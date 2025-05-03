from gtts import gTTS
import os
import platform

def output_text(text):
    print(f"Output: {text}")

def text_to_speech(text, lang='es'):
    tts = gTTS(text=text, lang=lang)
    tts.save("static/translated_audio.mp3")

