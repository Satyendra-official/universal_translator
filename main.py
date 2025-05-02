from app import input_handlers, translator, output_handlers

COMMON_LANGUAGES = {
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

def display_common_languages():
    print("\n🌍 Common Languages:")
    for code, name in COMMON_LANGUAGES.items():
        print(f"{code} - {name}")

def main():
    print("🎬 Universal Translator CLI")
    mode = input("Choose input mode (text/audio/video): ").strip().lower()
    
    display_common_languages()
    target_lang = input("Enter target language code (e.g., 'es'): ")

    if mode == "text":
        text = input_handlers.get_text_input()

    elif mode == 'audio':
        path = input("Enter path to audio file: ")
        wav_path = input_handlers.convert_mp3_to_wav(path)  
        text = input_handlers.get_text_from_audio(wav_path)

    elif mode == "video":
        path = input("Enter path to video file: ")
        extracted_audio = input_handlers.extract_audio_from_video(path)
        text = input_handlers.get_text_from_audio(extracted_audio)
    else:
        print("Invalid mode.")
        return

    translated = translator.translate_text(text, dest_lang=target_lang)
    print(f"\nTranslated: {translated}")
    output_handlers.output_text(translated)
    output_handlers.text_to_speech(translated, lang=target_lang)

if __name__ == "__main__":
    main()
