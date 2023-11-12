import nltk
from nltk.tokenize import word_tokenize

sample_text = "Mary works as a Software Engineer in ZY Corporation and lives in California!"

word = word_tokenize(sample_text)

#Let's grammatically classify the sample text using pos_tag
tagged = nltk.pos_tag(word)
print("Words with tags attached:")
print(tagged)

#Named Entity Recognition
namedE = nltk.ne_chunk(tagged, binary = True)
namedE.draw()
