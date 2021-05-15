import json
# from pprint import pprint





def extractData():
    # Opening JSON file
    
    print('Reading data from JSON file...')

    f = open('reviews_sm.json', encoding="utf-8")   

    data = json.loads("[" + f.read().replace("}\n{", "},\n{") + "]")

    texts = [i['text'] for i in data]

    stringTexts = ''.join(str(x) for x in texts) # extracted texts

    # print(len(texts))

    return stringTexts

    # Closing file
    # f.close()



