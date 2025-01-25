from textblob import TextBlob
text=" The difficulty  to understand  the deep  menaning of certain poems is immense "
blob=TextBlob(text)
print(blob.noun_phrases)

