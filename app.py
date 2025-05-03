from flask import Flask, render_template, request
from app.translator import translate_text
from app.output_handlers import text_to_speech

app = Flask(__name__)

LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "zh": "Chinese (Mandarin)",
    "hi": "Hindi",
    "ar": "Arabic",
    "ru": "Russian",
    "ja": "Japanese",
    "pt": "Portuguese"
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
