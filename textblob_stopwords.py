from nltk.corpus import stopwords
stops = stopwords.words('english')
from textblob import TextBlob
blob = TextBlob('It is an extremely difficult lesson .')
for word in blob.words:
 if word not in stops:
  print(word ,end="   ")










