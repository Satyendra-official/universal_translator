from gtts import gTTS
import os
import platform

def output_text(text):
    print(f"Output: {text}")

def text_to_speech(text, lang='es'):
    tts = gTTS(text=text, lang=lang)
    tts.save("static/translated_audio.mp3")

    # Play audio based on operating system
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("start translated_audio.mp3")
    elif system_platform == "Darwin":  # macOS
        os.system("afplay translated_audio.mp3")
    elif system_platform == "Linux":
        os.system("xdg-open translated_audio.mp3")
    else:
        print("Cannot auto-play audio on this OS.")
