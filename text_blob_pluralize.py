
from textblob import TextBlob
from textblob import Word
blob = Word("house")
pluralized_word = blob.pluralize()
print("The plural of  %s is  %s "% (blob, pluralized_word ))
