from fastapi import FastAPI
from pydantic import BaseModel

from nerOfData import getdData

class ReviewsModel(BaseModel):
    texts: str
    
app = FastAPI()

@app.post('/send_reviews')
async def sendData(text: ReviewsModel):
    print(text.texts)
    await getdData(text.texts)
    return text.texts

# @app.get('/reviews')
# async def sendData():
#     data = extractData()
#     return data