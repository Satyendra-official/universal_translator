from deep_translator import GoogleTranslator
from language_tool_python import LanguageTool
import re

# Idiom dictionary for common English idioms
IDIOM_DICT = {
    "en": {
        "kick the bucket": {
            "es": "morir",
            "fr": "passer l'arme à gauche",
            "de": "das Zeitliche segnen"
        },
        "raining cats and dogs": {
            "es": "llover a cántaros",
            "fr": "pleuvoir des cordes",
            "de": "wie aus Eimern gießen"
        },
        "break a leg": {
            "es": "¡mucha mierda!",
            "fr": "merde !",
            "de": "Hals- und Beinbruch!"
        }
    }
}

def preprocess_idioms(text, source_lang, target_lang):
    """Replace idioms in the input text with target-language equivalents."""
    if source_lang in IDIOM_DICT:
        for idiom, translations in IDIOM_DICT[source_lang].items():
            if re.search(r'\b' + re.escape(idiom) + r'\b', text, re.IGNORECASE):
                text = text.replace(idiom, translations.get(target_lang, idiom))
    return text

def postprocess_grammar(text, target_lang):
    """Correct grammatical errors in the translated text."""
    try:
        tool = LanguageTool(target_lang)
        matches = tool.check(text)
        corrected = tool.correct(text)
        return corrected
    except Exception as e:
        print(f"Grammar correction failed: {e}")
        return text

def translate_text(text, dest_lang='es', context='general'):
    """Translate text with preprocessing and postprocessing."""
    if not text.strip():
        return ""

    # Assume source is English for idiom preprocessing (adjust if auto-detection is needed)
    source_lang = 'en'
    text = preprocess_idioms(text, source_lang, dest_lang)
    
    # Translate using GoogleTranslator
    try:
        translated = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        # Correct grammar
        translated = postprocess_grammar(translated, dest_lang)
        return translated
    except Exception as e:
        print("Translation failed:", e)
        return text