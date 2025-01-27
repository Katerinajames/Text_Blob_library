#from textblob import TextBlob
from textblob import Word
b = Word("poor")
print("Sets of Synonyms")
print((b.synsets))
print("Lemmas ")
lemmas = b.synsets[0].lemmas()
print(lemmas)
print("Antonyms")
print (lemmas[0].antonyms())












