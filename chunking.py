import nltk
from nltk.tokenize import word_tokenize

sample_text = "Mary works as a Software Engineer in ZY Corporation and lives in California!"

word = word_tokenize(sample_text)

#Let's grammatically classify the sample text using pos_tag
tagged = nltk.pos_tag(word)
print("Words with tags attached:")
print(tagged)

#Let's grammatically group the words/phrases otherwise called as 'chunking'. Grouping all Noun Phrases.
chunkPattern = r"""chunk:{<DT>?<JJ>*<NN.*>+}""" 
chunkParser = nltk.RegexpParser(chunkPattern)
chunked = chunkParser.parse(tagged)
chunked.draw()

