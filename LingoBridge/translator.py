from deep_translator import GoogleTranslator

def translate_text(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

# User Input
user_input = input("Roman Urdu mein likhein:")

# Translation
translation = translate_text(user_input)
print("English Translation:\n", translation)