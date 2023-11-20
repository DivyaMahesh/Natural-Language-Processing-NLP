import nltk
import random
from nltk.corpus import movie_reviews

words =[]

for w in movie_reviews.words():
    words.append(w.lower())
words = nltk.FreqDist(words)

print("1.The most common words and their frequency distribution:")
print(words.most_common(15))
print("2.The Number of times the word 'character' shows up in the reviews:")
print(words["character"])

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
print("3.The list of movie reviews according to their category whether + or -:")
print(documents[1])
