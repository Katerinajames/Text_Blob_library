
from textblob import TextBlob

blob = TextBlob("bag ,star ,car,ox,foot,goose, likes")
x=blob.words 

for i in x:
	print (i.pluralize(),end=" ")


