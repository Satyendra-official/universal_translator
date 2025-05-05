from flask import Flask, render_template, request, redirect, url_for
import os
from app.translator import translate_text
from app.output_handlers import text_to_speech
from app.input_handlers import get_text_input, get_text_from_audio, extract_audio_from_video

app = Flask(__name__)

# Directory for uploading files
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Supported languages for translation
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
    audio_file_path = None

    if request.method == "POST":
        input_mode = request.form['input_mode']  # Get input mode (text/audio/video)
        target_lang = request.form["target_lang"]  # Get target language

        # Handle text input
        if input_mode == 'text':
            text = get_text_input(request.form["text"])

        # Handle audio file input (upload)
        elif input_mode == 'audio' and 'audio_file' in request.files:
            audio_file = request.files['audio_file']
            audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
            audio_file.save(audio_path)

            # Convert audio to text
            text = get_text_from_audio(audio_path)

        # Handle video file input (upload)
        elif input_mode == 'video' and 'video_file' in request.files:
            video_file = request.files['video_file']
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
            video_file.save(video_path)

            # Extract audio from video and convert to text
            audio_path = extract_audio_from_video(video_path)
            text = get_text_from_audio(audio_path)

        # Translate the text
        translated_text = translate_text(text, dest_lang=target_lang)

        # Generate speech from translated text
        audio_file_path = text_to_speech(translated_text, lang=target_lang)

    return render_template(
        "index.html",
        languages=dict(sorted(LANGUAGES.items(), key=lambda item: item[1])),
        translated_text=translated_text,
        audio_file_path=audio_file_path
    )

if __name__ == "__main__":
    app.run(debug=True)


