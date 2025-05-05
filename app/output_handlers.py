from gtts import gTTS
import os
import platform

# Print the translated text to the console or to the web page
def output_text(text):
    print(f"Output: {text}")

# Convert translated text to speech and save as MP3
def text_to_speech(text, lang='es'):
    tts = gTTS(text=text, lang=lang)
    # Save audio to a specific path for web access
    audio_path = os.path.join("static", "translated_audio.mp3")
    tts.save(audio_path)
    return audio_path  # Return path to the audio file

