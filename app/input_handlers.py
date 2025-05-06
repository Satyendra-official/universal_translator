import os
import ffmpeg
import speech_recognition as sr

# Ensure temp directory exists
TEMP_DIR = 'static/uploads'
os.makedirs(TEMP_DIR, exist_ok=True)

# Extract audio from video and save as a temporary wav file
def extract_audio_from_video(video_path, audio_path=None):
    if audio_path is None:
        audio_path = os.path.join(TEMP_DIR, 'temp_audio.wav')
    try:
        ffmpeg.input(video_path).output(
            audio_path,
            format='wav',
            acodec='pcm_s16le',
            ac=1,
            ar='16000'
        ).run(overwrite_output=True)
        return audio_path
    except ffmpeg.Error as e:
        print("Error extracting audio:", e)
        return None

# Convert MP3 audio to WAV format for recognition
def convert_mp3_to_wav(mp3_path, wav_path='temp_audio.wav'):
    try:
        # Ensure proper codec and parameters for compatibility with speech_recognition
        ffmpeg.input(mp3_path).output(
            wav_path,
            format='wav',
            acodec='pcm_s16le',
            ac=1,             # Mono audio
            ar='16000'        # Sample rate 16kHz
        ).overwrite_output().run()

        # Validation: ensure file exists and is not empty
        if not os.path.exists(wav_path) or os.path.getsize(wav_path) == 0:
            raise Exception("WAV file was not created or is empty.")
        return wav_path

    except ffmpeg.Error as e:
        print("FFmpeg conversion error:", e.stderr.decode() if e.stderr else str(e))
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

