from nltk.tokenize import sent_tokenize, word_tokenize

sample_text = "Hey, let's see how nltk begins with the first step called tokenization. We can seperate a paragraph into sentences. Also, a sentence into words."

#Following statement will print the sample_text as a list of sentences
print(sent_tokenize(sample_text))

#Following statement will print the sample_text as a list of words
print(word_tokenize(sample_text))



