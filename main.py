from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient

from ner_of_data import get_data


# model to validate data
class ReviewsModel(BaseModel):
    texts: str


app = FastAPI()


# @route   POST /send_reviews
# @desc    send reviews to ner
# @access  public
@app.post('/send_reviews')
async def send_data(text: ReviewsModel):
    print(text.texts)
    await get_data(text.texts)
    return text.texts


