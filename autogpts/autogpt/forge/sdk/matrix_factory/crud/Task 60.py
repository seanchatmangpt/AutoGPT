# Import the gettext module
import gettext

# Set the language to English
lang = 'en'

# Create a translation object for the specified language
translation = gettext.translation('messages', localedir='locales', languages=[lang])

# Activate the translation
translation.install()

# Define a function to handle translations
def _translate(text):
    return gettext.gettext(text)

# Use the function to translate a string
print(_translate('Hello, world!'))