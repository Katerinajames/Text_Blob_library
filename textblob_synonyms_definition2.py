from textblob import Word
b = Word("friend").synsets
print (b)
for synset in b:
 print (synset.definition()+"\n")











