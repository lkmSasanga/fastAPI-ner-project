import spacy

nlp = spacy.load("en_core_web_sm")

# increase nlp length
nlp.max_length = 4000000


# call ner_process asynchronous
async def get_data(data):
    return ner_process(data)


# ner process
def ner_process(texts):
    try:
        doc = nlp(texts)
        print('ner process started...')
        for ent in doc.ents:
            print(ent.text, ent.label_)
    finally:
        print('No any entities found!')
