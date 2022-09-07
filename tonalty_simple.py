from textblob import TextBlob
text = TextBlob('''US Embassy welcomes departure of first grain ship from Odesa''')
print(text.polarity)


