import spacy

nlp = spacy.load("en_core_web_sm")


# nlp.max_length = 4000000  # or even higher


async def get_data(data):
    return ner_process(data)

    # NER process


def ner_process(texts):
    try:
        doc = nlp(texts)
        print('***NER process started...')
        for ent in doc.ents:
            print(ent.text, ent.label_)

    finally:
        print('Error Occurred')
