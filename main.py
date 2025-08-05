from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from openai import AzureOpenAI
from dotenv import load_dotenv
import openai
import os

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "answer": None})

@app.post("/", response_class=HTMLResponse)
async def ask_ai(request: Request, question: str = Form(...)):
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),  # deployment name
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    answer = response.choices[0].message.content
    return templates.TemplateResponse("index.html", {"request": request, "answer": answer, "question": question})



"""
pip install -r requirements.txt
uvicorn main:app --reload
"""




