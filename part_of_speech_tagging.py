import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

sample_text = "This this is a a a a sample text text text text text to to explain the part of speech tagging!"

word = word_tokenize(sample_text)

#Let's grammatically classify the sample text using pos_tag
tagged = nltk.pos_tag(word)
print("Words with tags attached:")
print(tagged)

#Let's count the each tag present in the sample text using dictionary counter where the words are keys and tags are values.
print("Tag Counts:")
counter = Counter(t for word, t in tagged)
print(counter)

#Let's plot the frequency distribution of words in the sample text. You need Matplotlib installed to use this feature.
fd = nltk.FreqDist(word)
fd.plot()

