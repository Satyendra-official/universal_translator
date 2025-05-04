from flask import Flask, render_template, request
from app.translator import translate_text
from app.output_handlers import text_to_speech

app = Flask(__name__)

LANGUAGES = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "hi": "Hindi",
    "zh-CN": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "pt": "Portuguese",
    "ru": "Russian",
    "it": "Italian",
    "bn": "Bengali",
    "ur": "Urdu",
    "tr": "Turkish",
    "ta": "Tamil",
    "nl": "Dutch",
    "gu": "Gujarati",
    "mr": "Marathi",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada",
    "vi": "Vietnamese",
    "uk": "Ukrainian",
    "pl": "Polish",
    "th": "Thai"
}



@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text = request.form["text"]
        lang = request.form["target_lang"]
        translated_text = translate_text(text, dest_lang=lang)
        text_to_speech(translated_text, lang=lang)
    return render_template("index.html", languages=LANGUAGES, translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
