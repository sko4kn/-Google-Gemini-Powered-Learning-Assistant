from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import recommend_learning_path

app = FastAPI(title="EduGenie", description="Google Gemini Powered Learning Assistant", version="1.0.0")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TextRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
async def health():
    return {"status": "ok", "message": "EduGenie is running"}


@app.post("/qa")
async def qa(request: TextRequest):
    return {"answer": answer_question(request.text)}


@app.post("/explain")
async def explain(request: TextRequest):
    return {"explanation": explain_concept(request.text)}


@app.post("/quiz")
async def quiz(request: TextRequest):
    return {"quiz": generate_quiz(request.text)}


@app.post("/summarize")
async def summarize(request: TextRequest):
    return {"summary": summarize_text(request.text)}


@app.post("/learn/recommendations")
async def learning_recommendations(request: TextRequest):
    return {"recommendations": recommend_learning_path(request.text)}
