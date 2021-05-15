import spacy
from fastapi import FastAPI

from importJson import extractData

app = FastAPI()

nlp = spacy.load("en_core_web_sm")

# nlp.max_length = 4000000  # or even higher

# data = extractData()

from pydantic import BaseModel
class ReviewsModel(BaseModel):
    texts: str


@app.post('/send_reviews')
async def getdData(texts: ReviewsModel):
    # data = extractData()
    print('Send data function called')
    ner = nerProcess(texts)
    return ner

def nerProcess(texts):
    # NER process
    try:
        doc = nlp(texts)

        print('NER process started...')

        for ent in doc.ents:
            print(ent.text, ent.label_)
            # return ent.text, ent.label_
    except Exception:
        print('Error Occured') 