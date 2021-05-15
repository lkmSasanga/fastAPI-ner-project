import json
# from pprint import pprint

def extractData():
    # Opening JSON file
    f = open('reviews_sm.json', encoding="utf8")   

    data = json.loads("[" + f.read().replace("}\n{", "},\n{") + "]")

    texts = [i['text'] for i in data]

    print(len(texts))

    return texts

    # Closing file
    f.close()



