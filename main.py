# from app import input_handlers, translator, output_handlers

# def main():
#     print("Welcome to the Universal Translator CLI")
#     text = input_handlers.get_text_input()
#     target_lang = input("Enter target language code (e.g., 'es' for Spanish, 'fr' for French): ")

#     translated = translator.translate_text(text, dest_lang=target_lang)
#     print(f"Translated Text: {translated}")

#     output_handlers.output_text(translated)
#     output_handlers.text_to_speech(translated, lang=target_lang)

# if __name__ == "__main__":
#     main()


from app import input_handlers, translator, output_handlers

def main():
    print("Welcome to the Universal Translator CLI")
    print("Choose input type:")
    print("1. Text")
    print("2. Audio file")
    print("3. Video file")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        text = input_handlers.get_text_input()
    elif choice == '2':
        path = input("Enter path to audio file (e.g., audio.mp3 or audio.wav): ")
        text = input_handlers.get_audio_input(path)
    elif choice == '3':
        path = input("Enter path to video file (e.g., video.mp4): ")
        text = input_handlers.get_video_input(path)
    else:
        print("Invalid choice.")
        return

    print(f"\nDetected Input: {text}")
    target_lang = input("Enter target language code (e.g., 'es' for Spanish): ")
    translated = translator.translate_text(text, dest_lang=target_lang)

    print(f"\nTranslated Text: {translated}")
    output_handlers.output_text(translated)
    output_handlers.text_to_speech(translated, lang=target_lang)

if __name__ == "__main__":
    main()
