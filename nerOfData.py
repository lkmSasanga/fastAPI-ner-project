import spacy

from importJson import extractData

nlp = spacy.load("en_core_web_sm")

nlp.max_length = 4000000  # or even higher

# data = extractData()

# print(len(data))

def nerProcess(data):
    # NER process
    doc = nlp(data)

    print('NER process started...')

    for ent in doc.ents:
        print(ent.text, ent.label_)
        # return ent.text, ent.label_