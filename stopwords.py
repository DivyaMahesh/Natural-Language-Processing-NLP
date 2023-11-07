from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sample_text = "Hello, let's take this as an example sentence to filter out stop words."

stop_words = set(stopwords.words('English')) #you can set this to any language you want

#print(stop_words) to see the list of stop words used in nlp

words = word_tokenize(sample_text)

filtered_text = [w for w in words if w not in stop_words] #one-liner format

print(filtered_text)
