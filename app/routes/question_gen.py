from fastapi import APIRouter, Body

from app.schemas.question_gen import QuestionInput
from app.services.question_model import generate_follow_up_questions

router = APIRouter()


@router.post("/generate-questions")
def generate_questions(data: QuestionInput):
    input_text = data.input_text
    return {"follow_up_question": f"What are the benefits of {input_text.lower()}?"}
