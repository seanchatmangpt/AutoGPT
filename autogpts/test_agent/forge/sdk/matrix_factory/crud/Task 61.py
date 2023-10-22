# Import the gettext module
import gettext

# Create a translation object for the desired language
lang = gettext.translation('messages', localedir='locales', languages=['fr'])

# Activate the translation
lang.install()

# Define a function to handle translations
def _translate(text):
    return lang.gettext(text)

# Use the function to translate the given input
_translate("Test internationalization")