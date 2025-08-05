from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import openai
import os

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

openai.api_type = "azure"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_VERSION")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": None})

@app.post("/", response_class=HTMLResponse)
async def ask_ai(request: Request, question: str = Form(...)):
    response = openai.ChatCompletion.create(
        engine=deployment,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    answer = response['choices'][0]['message']['content']
    return templates.TemplateResponse("index.html", {"request": request, "answer": answer, "question": question})



"""
pip install -r requirements.txt
uvicorn main:app --reload
"""