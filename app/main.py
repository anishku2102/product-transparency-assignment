from fastapi import FastAPI
from app.routes import question_gen  # scoring can be added later

app = FastAPI(title="AI Question Generator")

app.include_router(question_gen.router)