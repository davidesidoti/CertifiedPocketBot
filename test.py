from googletrans import Translator

# Instantiate the Google Translator.
translator = Translator()
translator.raise_Exception = True

# Translate the text to Turkish.
translation = translator.translate('Hello, my name is Davide.', dest='tr')
print(translation)
