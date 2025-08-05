# 🤖 Ask AI - Azure OpenAI Web App

This is a simple web application that allows users to ask questions and get answers from an Azure OpenAI model (like GPT-3.5 or GPT-4), deployed via Azure Foundry.

---

## 🌐 Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML + Jinja2 Templates
- **AI Model**: Azure OpenAI (Chat Completion API)
- **Deployment**: Local (can be deployed to Azure App Service)

---

## 🚀 Features

- Ask any question in a web form
- Get AI-generated responses using your Azure OpenAI deployment
- Secure use of API keys via `.env` file

---

## 📁 Project Structure

ask-ai-app/
├── main.py # FastAPI backend code
├── requirements.txt # Python dependencies
├── .env # Azure credentials (not committed)
└── templates/
└── index.html # Frontend form and output



---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ask-ai-app.git
cd ask-ai-app

pip install -r requirements.txt

AZURE_OPENAI_KEY=your-azure-openai-api-key
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_VERSION=2023-12-01-preview

To run Application
uvicorn main:app --reload
