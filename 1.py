import nltk
import numpy
from nltk.corpus import gutenberg
from nltk.corpus import wordnet as wn
import re

'''print(nltk.corpus.gutenberg.fileids())
sum=0
for book in gutenberg.fileids():
    booklen=len(gutenberg.words(book))
    sum +=booklen
    print(book,booklen)
print('\ntotal words:',sum)

print(' '.join(gutenberg.words('carroll-alice.txt')[100:200]))

text=' that poster costs $22.40，in the U.S.A. '
pattern=r'(?x) \$?\d+(?:\.\d+)? | (?:[A-Z]\.)+| \w+| [^\w\s]+'
tokens = nltk.tokenize.regexp_tokenize(text, pattern)
#tokens= nltk.regexp_tokenize(text,pattern)
print(tokens)

stemmer=nltk.PorterStemmer()
stemword=[] #list
for verb in ['appears','appeared','calls','calling','called']:
    stemword.append(stemmer.stem(verb))
print(stemword)

car=wn.synsets('car')
print(car)
print(car[0].definition())
print(car[0].examples())'''

w1=wn.synsets('ship')[0]
w2=wn.synsets('boat')[0]
similarity=w1.wup_similarity(w2)
print(similarity)



'''actual=wn.synsets('cat')[0]
predicted=wn.synsets('orange')[0]
similarity=actual.wup_similarity(predicted)
print(similarity)'''
