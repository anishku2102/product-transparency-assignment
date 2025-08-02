# app/routes/scoring.py

from fastapi import APIRouter, Body
from app.services.scoring_logic import compute_transparency_score

router = APIRouter()

@router.post("/transparency-score")
def score_text(input_text: str = Body(...)):
    score = compute_transparency_score(input_text)
    return {"transparency_score": score}
