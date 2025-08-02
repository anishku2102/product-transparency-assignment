from pydantic import BaseModel

class QuestionInput(BaseModel):
    input_text: str
