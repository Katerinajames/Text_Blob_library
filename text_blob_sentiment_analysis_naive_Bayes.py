
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
text="It is a rainy day and fortunately I do not have to go to work!!!!!"
blob=TextBlob(text, analyzer=NaiveBayesAnalyzer())
print(blob.sentiment) 
