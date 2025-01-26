from textblob import TextBlob
text = """
Life is a matter of choices and  every choice you make makes you. 
Happiness is a matter of perspective."""
blob=TextBlob(text)

print(blob.sentences)
