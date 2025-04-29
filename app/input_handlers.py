# import speech_recognition as sr
# from pydub import AudioSegment
# import os
# from moviepy.editor import VideoFileClip

# def get_text_input():
#     return input("Enter text to translate: ")

# def handle_audio_input(file_path):
#     recognizer = sr.Recognizer()
    
#     # Convert to WAV if necessary
#     if not file_path.endswith(".wav"):
#         sound = AudioSegment.from_file(file_path)
#         file_path = "temp_audio.wav"
#         sound.export(file_path, format="wav")

#     with sr.AudioFile(file_path) as source:
#         audio_data = recognizer.record(source)
#         try:
#             text = recognizer.recognize_google(audio_data)
#             return text
#         except sr.UnknownValueError:
#             return "Could not understand audio."
#         except sr.RequestError as e:
#             return f"Speech recognition error: {e}"
        
# def handle_video_input(video_path):
#     video = VideoFileClip(video_path)
#     audio_path = "extracted_audio.wav"
#     video.audio.write_audiofile(audio_path)
#     return handle_audio_input(audio_path)


import speech_recognition as sr
from pydub import AudioSegment
from moviepy.editor import VideoFileClip

def get_text_input():
    return input("Enter your text: ")

def get_audio_input(audio_path):
    recognizer = sr.Recognizer()

    # Convert audio to WAV if needed
    if not audio_path.endswith(".wav"):
        sound = AudioSegment.from_file(audio_path)
        audio_path = "converted_audio.wav"
        sound.export(audio_path, format="wav")

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            return "Audio could not be understood."
        except sr.RequestError as e:
            return f"Speech recognition error: {e}"

def get_video_input(video_path):
    audio_path = "extracted_audio.wav"
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    return get_audio_input(audio_path)
