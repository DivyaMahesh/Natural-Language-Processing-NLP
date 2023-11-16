#Wordnet is a lexical database for english language that organize words into synonyms, antonyms and provides comparative studies- similarity among the words.
from nltk.corpus import wordnet

syn = wordnet.synsets("care")

# print(syn) To print the entire synonyms set

#print(syn[0]) To print the first item from the synset

#print(syn[0].name()) To print only the word of the first item

print("1. To print just the name without any tags:")
print(syn[0].lemmas()[0].name())

print("2. Definition of the first word:")
print(syn[0].definition())

print("3. Examples using the first word:")
print(syn[0].examples()) 

#Wu-Palmer algorithm calculates the similarity between two words

print("4. Similarity Percentage between the words 'happy' and 'goat:")
word1 = wordnet.synsets('happy')[0]
word2 = wordnet.synsets('goat')[0]
print(str(word2.wup_similarity(word1)*100)+"%")

print("5. Similarity Percentage between the words 'happy' and 'merry:")
word3 = wordnet.synsets('happy')[0]
word4 = wordnet.synsets('merry')[0]
print(str(word4.wup_similarity(word3)*100)+"%")

#To print the synonyms and antonyms set of a particular word
synonyms = []
antonyms = []

for s in wordnet.synsets("truth"):
    for l in s.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print("6. Synonyms of the word 'truth':")         
print(set(synonyms))
print("7. Antonyms of the word 'truth':")         
print(set(antonyms))
