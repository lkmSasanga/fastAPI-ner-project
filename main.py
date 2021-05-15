from fastapi import FastAPI
import spacy

from importJson import extractData

app = FastAPI()

nlp = spacy.load("en_core_web_sm")

# Getting the pipeline component
ner = nlp.get_pipe("ner")

# Training data
TRAIN_DATA = [
    ("Awesome place,gets crowded easily in the evenings,most famous restaurant in Ella", {"entities": [(76, 80, "GPE")]})
]

# Adding labels to the `ner`
for _, annotations in TRAIN_DATA:
  for ent in annotations.get("entities"):
    ner.add_label(ent[2])

# Disable pipeline components you dont need to change
pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]



nlp.max_length = 4000000  # or even higher

# f = open('reviews_sm.json', encoding="utf8")

# text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# data = json.loads("[" + f.read().replace("}\n{", "},\n{") + "]")

# texts = [i['text'] for i in data]

# stringTexts = ''.join(str(x) for x in texts)


def convertToStr(texts, seperator):
   final_str = seperator.join(str(x) for x in texts)
   return final_str

texts = extractData()

seperator = ' '
stringTexts = convertToStr(texts, seperator)




print(type(stringTexts))


doc = nlp(stringTexts)

for ent in doc.ents:
    print(ent.text, ent.label_)

print(len(stringTexts))

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