import spacy
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

nlp = spacy.load("en_core_web_sm")

# increase nlp length
nlp.max_length = 4000000


# call ner_process asynchronous
async def get_data(data):
    return ner_process(data)


# ner process
def ner_process(texts):
    doc = nlp(texts)
    print('ner process started...')

    entities = []
    for ent in doc.ents:
        print(ent.text, ent.label_)
        # return ent.text, ent.label_
        entities += [{
            "entity": ent.text,
            "entity_label": ent.label_
        }]

    # return entities

    # json_compatible_item_data = jsonable_encoder(entities)
    return JSONResponse(entities)

    # print(entities)

    # try:
    #
    # finally:
    #     print('No any entities found!')
