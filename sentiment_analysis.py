import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

from import_json import extract_data

nlp = spacy.load("en_core_web_sm")

nlp.add_pipe("spacytextblob")

# extract data from json
my_text = extract_data()
doc = nlp(my_text)

# get polarity score of the text
sentiment_polarity = doc._.polarity
print(sentiment_polarity)

# get polarity score of the text
sentiment_subjectivity = doc._.subjectivity
print(sentiment_subjectivity)

# get polarity score of the text
sentiment_assessments = doc._.assessments
print(sentiment_assessments)

