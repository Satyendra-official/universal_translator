from deep_translator import GoogleTranslator

# Translate the given text to the target language
def translate_text(text, dest_lang='es'):
    try:
        translated = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        return translated
    except Exception as e:
        print("Translation failed:", e)
        return text


