# app/services/question_model.py

from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")


def generate_follow_up_questions(context: str) -> str:
    prompt = f"Generate a follow-up question for: {context}"
    output = generator(prompt, max_length=64, do_sample=True)
    return output[0]['generated_text']
