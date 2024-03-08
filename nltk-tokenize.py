# Dieses Programm lief erst nach "Installing NLTK Data" https://www.nltk.org/data.html
# 1. Aufruf von Python 3.10.2 (Python-Konsole (mit Prompt))
# 2. -->
# >>> import nltk
# >>> nltk.download('popular')

import nltk
from nltk import word_tokenize

# text_line="Hola mundo! El mundo es un lugar muy bonito. ¿Verdad?"
text_line="Hello world! The world is a nice place to be. Isn't it?"
text=word_tokenize(text_line)
print(text)

print(nltk.pos_tag(text))
