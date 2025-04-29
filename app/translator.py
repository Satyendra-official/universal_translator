from deep_translator import GoogleTranslator

def translate_text(text, dest_lang='es'):
    try:
        translated = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        return translated
    except Exception as e:
        print("Translation failed:", e)
        return text
