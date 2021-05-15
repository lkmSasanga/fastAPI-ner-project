import spacy

from importJson import extractData


nlp = spacy.load("en_core_web_sm")


data = extractData()

doc = nlp(data)

# Tokenizing
token_list = [token for token in doc]

# Removing stop words
filtered_tokens = [token for token in doc if not token.is_stop]

# Normalization - lemma
lemmas = [ f"Token: {token}, lemma: {token.lemma_}" 
    for token in filtered_tokens ]

# print(filtered_tokens)
print(lemmas)