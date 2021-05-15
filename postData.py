from fastapi import FastAPI
# from typing import List
from pydantic import BaseModel

from importJson import extractData
from nerOfData import getdData

class ReviewsModel(BaseModel):
    texts: str
    
app = FastAPI()


@app.post('/send_reviews')
async def sendData(texts: ReviewsModel):
    print(texts)
    await getdData(texts)
    return texts

# @app.get('/reviews')
# async def sendData():
#     data = extractData()
#     return data