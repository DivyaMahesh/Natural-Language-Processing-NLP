import nltk
from nltk.tokenize import word_tokenize

sample_text = "This is a sample text to explain the process of chunking!"

word = word_tokenize(sample_text)

#Let's grammatically classify the sample text using pos_tag
tagged = nltk.pos_tag(word)
print("Words with tags attached:")
print(tagged)

#Let's grammatically group the words otherwise called as 'chunking'
chunkPattern = r"""chunk:{<VB.?>*<NN>+<DT>?}"""
chunkParser = nltk.RegexpParser(chunkPattern)
chunked = chunkParser.parse(tagged)
chunked.draw()

