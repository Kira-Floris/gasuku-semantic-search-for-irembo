import pydantic
import typing

import fastapi
from fastapi import Request
from fastapi.responses import RedirectResponse
app = fastapi.FastAPI()

import uvicorn

import utils as search

class QuestionBase(pydantic.BaseModel):
    question:str
    
@app.get('/')
async def home(request:Request):
    return RedirectResponse('/docs')

@app.post('/bot-answer/')
async def get_answer(question:QuestionBase):
    answers = search.get_answer(question.question)
    return answers

if __name__=='__main__':
    app_str = 'app:app'
    uvicorn.run(app_str, host='0.0.0.0', port=8000, reload=True)
    