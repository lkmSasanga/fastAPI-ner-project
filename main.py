
from importJson import extractData
from postData import sendData
from nerOfData import nerProcess

data = extractData()

print(nerProcess(data))

# Getting the pipeline component
# ner = nlp.get_pipe("ner")

# Training data
# TRAIN_DATA = [
#     ("Awesome place,gets crowded easily in the evenings,most famous restaurant in Ella", {"entities": [(76, 80, "GPE")]})
# ]

# Adding labels to the `ner`
# for _, annotations in TRAIN_DATA:
#   for ent in annotations.get("entities"):
#     ner.add_label(ent[2])

# Disable pipeline components you dont need to change
# pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
# unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]


# stringTexts = extractData()

# seperator = ' '
# stringTexts = convertToStr(texts, seperator)

# print(type(stringTexts))



# @app.get("/")
# def home():
#     return {"Hello": "FastAPI"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}