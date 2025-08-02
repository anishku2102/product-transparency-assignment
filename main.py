from fastapi import FastAPI
from app.routes import question_gen, scoring

app= FastAPI(title="AI Question Generator")

app.include_router(question_gen.router)

try:
    app.include_router(scoring.router)
except:
    pass