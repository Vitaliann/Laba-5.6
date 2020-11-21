from googletrans import Translator
translator = Translator()

# Переводим с русского на английский
w=translator.translate('Привет. Как дела?', dest='en')
print(w.text)
w=translator.translate('Как ты?', dest='de')
print(w.text)

# Переводим с английского на русский
w=translator.translate('How much is the fish in ocean?', dest='ru')
print(w.text)
