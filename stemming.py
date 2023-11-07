from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

s = PorterStemmer()

print(" 1. Stemming the list of words ")
sample_text_1 = ["run", "runs", "running", "ran", "runner"]

for i in sample_text_1:
    print(s.stem(i))

print(" 2. Stemming the list of words extracted from a sentence ")
sample_text_2 = "Lisa has run in the state tournament and has scored 33 runs securing a runner up position in the running competition"
                 
chunks = word_tokenize(sample_text_2)
for j in chunks:
    print(s.stem(j))
