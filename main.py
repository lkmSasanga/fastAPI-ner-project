import json
from fastapi import FastAPI
import spacy

app = FastAPI()

nlp = spacy.load("en_core_web_sm")
nlp.max_length = 4000000  # or even higher

f = open('reviews_sm.json', encoding="utf8")

# text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

data = json.loads("[" + f.read().replace("}\n{", "},\n{") + "]")

texts = [i['text'] for i in data]

# stringTexts = ''.join(str(x) for x in texts)



def convertToStr(texts, seperator):
   final_str = seperator.join(str(x) for x in texts)
   return final_str

seperator = ' '
stringTexts = convertToStr(texts, seperator)

print(len(stringTexts))
print(type(stringTexts))

# def listToString(texts): 

#     # initialize an empty string
#     str1 = " " 

#     # return string  
#     return (str1.join(texts))

# print(listToString(texts)) 
# print(type(listToString(texts))) 


doc = nlp(stringTexts)

for ent in doc.ents:
    print(ent.text, ent.label_)


# import spacy
# from spacy import displacy
# from collections import Counter
# import en_core_web_sm
# nlp = en_core_web_sm.load()

# doc = nlp('European authorities fined Google a record $5.1 billion on Wednesday for abusing its power in the mobile phone market and ordered the company to alter its practices')
# print([(X.text, X.label_) for X in doc.ents])


@app.get("/")
def home():
    return {"Hello": "FastAPI"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}