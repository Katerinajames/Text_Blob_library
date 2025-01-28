from textblob import TextBlob
text = '"N-grams enhance language processing tasks."'
blob = TextBlob(text)
print ("Unigram")
print (blob.ngrams(n=1))
print ("Bigram")
print (blob.ngrams(n=2))
print ("Trigram")
print (blob.ngrams(n=3))










