from deep_translator import GoogleTranslator

def translate_text(text):
    translated = GoogleTranslator(source='en', target='ur').translate(text)
    return translated

# User Input
user_input = input("Please type in English: ").strip()

if user_input:
    translation = translate_text(user_input)
    print("Urdu Translation:\n", translation)
else:
    print("Please type some text.")