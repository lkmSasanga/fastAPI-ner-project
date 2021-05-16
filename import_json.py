import json


def extract_data():
    print('Reading data from JSON file...')

    # open json file
    f = open('reviews_sm.json', encoding="utf-8")

    # converting objects to list of objects
    data = json.loads("[" + f.read().replace("}\n{", "},\n{") + "]")

    # extract text from objects
    texts = [i['text'] for i in data]

    # convert to strings
    string_texts = ''.join(str(x) for x in texts) # extracted texts

    return string_texts

    # Closing file
    f.close()



