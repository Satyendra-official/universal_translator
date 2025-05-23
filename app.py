from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime
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
    input_text = ""
    timestamp = datetime.now().timestamp()  # cache-busting timestamp

    if request.method == "POST":
        input_mode = request.form['input_mode']  # Get input mode (text/audio/video)
        target_lang = request.form["target_lang"]  # Get target language
        context = request.form.get("context", "general")  # Get context, default to "general"

        # Handle text input
        if input_mode == 'text':
            input_text = get_text_input(request.form["text"])

        # Handle audio file input (upload)
        elif input_mode == 'audio' and 'audio_file' in request.files:
            audio_file = request.files['audio_file']
            mp3_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
            audio_file.save(mp3_path)

            from app.input_handlers import convert_mp3_to_wav
            wav_path = os.path.join(app.config['UPLOAD_FOLDER'], 'converted_audio.wav')
            wav_path = convert_mp3_to_wav(mp3_path, wav_path)

            if wav_path:
                input_text = get_text_from_audio(wav_path)
            else:
                input_text = ""

        # Handle video file input (upload)
        elif input_mode == 'video' and 'video_file' in request.files:
            video_file = request.files['video_file']
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file.filename)
            video_file.save(video_path)

            audio_path = extract_audio_from_video(video_path)
            input_text = get_text_from_audio(audio_path)

        # Translate the text
        translated_text = translate_text(input_text, dest_lang=target_lang, context=context)

        # Generate speech from translated text
        audio_file_path = text_to_speech(translated_text, lang=target_lang)

    return render_template(
        "index.html",
        languages=dict(sorted(LANGUAGES.items(), key=lambda item: item[1])),
        translated_text=translated_text,
        input_text=input_text,  # Pass input text for feedback
        audio_file_path=audio_file_path,
        timestamp=timestamp
    )

@app.route("/feedback", methods=["POST"])
def save_feedback():
    data = request.json
    with open("feedback.txt", "a") as f:
        f.write(f"Input: {data['input_text']}, Translation: {data['translated_text']}, Expected: {data['expected']}, Context: {data['context']}\n")
    return {"status": "Feedback saved"}

if __name__ == "__main__":
    app.run(debug=True)