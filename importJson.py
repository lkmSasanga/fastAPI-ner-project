import json

def extractData():
    # Opening JSON file
    
    print('Reading data from JSON file...')

    f = open('reviews_sm.json', encoding="utf-8")

    # converting objects to list of objects
    data = json.loads("[" + f.read().replace("}\n{", "},\n{") + "]")

    texts = [i['text'] for i in data]

    # convert to strings
    stringTexts = ''.join(str(x) for x in texts) # extracted texts

    return stringTexts

    # Closing file
    # f.close()



