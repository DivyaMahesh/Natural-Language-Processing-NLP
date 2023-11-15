import nltk
from nltk.stem import WordNetLemmatizer

#WordNetLemmatizer is an algorithm by NLTK to lemmatize texts
lemma = WordNetLemmatizer()
sample_text = "Mary works as a Software Engineer in ZY Corporation and lives in California!"

#Lemmatization is a text normalization technique to reduce words to it's base form
#By default pos ='n' noun.
result = [lemma.lemmatize(word, pos='v') for word in sample_text.split()]
print(result)
