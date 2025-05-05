import os
import ffmpeg
import speech_recognition as sr

# Extract audio from video and save as a temporary wav file
def extract_audio_from_video(video_path, audio_path='temp_audio.wav'):
    try:
        ffmpeg.input(video_path).output(audio_path, format='wav').run(overwrite_output=True)
        return audio_path
    except ffmpeg.Error as e:
        print("Error extracting audio:", e)
        return None

# Convert MP3 audio to WAV format for recognition
def convert_mp3_to_wav(mp3_path, wav_path='temp_audio.wav'):
    try:
        ffmpeg.input(mp3_path).output(wav_path, format='wav', acodec='pcm_s16le', ac=1, ar='16000').run(overwrite_output=True)
        return wav_path
    except ffmpeg.Error as e:
        print("Error converting MP3 to WAV:", e)
        return None

# Handle text input from the user
def get_text_input(text):
    return text

# Recognize speech from audio file and return as text
def get_text_from_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Speech recognition error:", e)
    return ""

