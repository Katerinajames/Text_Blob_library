
from textblob import TextBlob
blob = TextBlob("bag ,star ,car,ox,foot,goose, likes")
for i in blob.words :
	print (i.pluralize(),end=" ")


