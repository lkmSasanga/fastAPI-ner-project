import spacy
from fastapi import FastAPI

nlp = spacy.load("en_core_web_sm")

# nlp.max_length = 4000000  # or even higher

async def get_data(data):
    ner = ner_process(data)
    return ner

    # NER process
def ner_process(texts):
    try:
        doc = nlp(texts)

        print('***NER process started...')

        for ent in doc.ents:
            print(ent.text, ent.label_)

    except Exception:
        print('Error Occured') 