from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

from importJson import extractData

class ReviewsModel(BaseModel):
    texts: str
    
app = FastAPI()




# def sendData(data):
#     # POST end 
    # return None

@app.get('/reviews')
async def sendData():
    data = extractData()
    return data