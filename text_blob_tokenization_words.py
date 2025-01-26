from textblob import TextBlob
text = "Life is a matter of choices and  every choice you make makes you"
blob=TextBlob(text)
print(blob.words)
