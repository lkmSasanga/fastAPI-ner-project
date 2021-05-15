import json
from pprint import pprint

# Opening JSON file
f = open('reviews.json', encoding="utf8")

# returns JSON object as 
# a dictionary
# data = json.load(f)

data = json.loads("[" + f.read().replace("}\n{", "},\n{") + "]")

# for i in data['text']:
#     print(i)

print(data)
# Closing file
f.close()
