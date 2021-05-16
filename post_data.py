from fastapi import FastAPI
from pydantic import BaseModel

from ner_of_data import get_data

class ReviewsModel(BaseModel):
    texts: str
    
app = FastAPI()

@app.post('/send_reviews')
async def send_data(text: ReviewsModel):
    print(text.texts)
    await get_data(text.texts)
    return text.texts

# @app.get('/reviews')
# async def sendData():
#     data = extractData()
#     return data