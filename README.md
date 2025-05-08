
# 🌍 Universal Translator

Universal Translator is a Python-based application that translates **text, audio, or video** inputs into a preferred language, delivering outputs as **text, speech, or video** with replaced or subtitled audio.

> ✅ Includes a CLI tool and a **Flask web interface** for seamless interaction.

---

## 📦 Features

- ✅ Translate **text input** to any supported language
- ✅ Convert translated text to **speech/audio**
- ✅ Web-based interface powered by Flask
- ✅ Audio input support (beta)
- 🛠️ In progress:
  - 📹 Video input with audio extraction
  - 🎬 Video output with subtitles or dubbed audio
  - 🎨 Enhanced UI/UX with modern styling

---

## 🛠 Requirements

- Python 3.11 (⚠️ Python 3.12 not recommended due to dependency compatibility)
- Virtual environment strongly recommended
- FFmpeg installed for audio/video processing (required for future features)

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/Satyendra-official/universal_translator.git
cd universal_translator
```

2. Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install FFmpeg (for audio/video features):

- **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html) or install via Chocolatey (`choco install ffmpeg`)
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt-get install ffmpeg` (Ubuntu/Debian) or equivalent

---

## 🚀 How to Use

### 🖥️ CLI Mode

```bash
python main.py
```

1. Select input type: `text`, `audio` (beta), or `video` (coming soon)
2. Enter target language code (e.g., `fr` for French)
3. View or hear the translated output

### 🌐 Web Interface (Flask)

```bash
python app.py
```

1. Navigate to [http://localhost:5000](http://localhost:5000) in your browser
2. Input text or upload audio (beta)
3. Select target language
4. View or listen to the translated result

---

## 🌐 Common Language Codes

| Language   | Code | Language             | Code    |
|------------|------|----------------------|---------|
| English    | `en` | French               | `fr`    |
| Spanish    | `es` | German               | `de`    |
| Hindi      | `hi` | Chinese (Simplified) | `zh-CN` |
| Japanese   | `ja` | Korean               | `ko`    |
| Arabic     | `ar` | Portuguese           | `pt`    |
| Russian    | `ru` | Italian              | `it`    |
| Bengali    | `bn` | Urdu                 | `ur`    |
| Turkish    | `tr` | Tamil                | `ta`    |
| Dutch      | `nl` | Gujarati             | `gu`    |
| Marathi    | `mr` | Telugu               | `te`    |
| Malayalam  | `ml` | Kannada              | `kn`    |
| Vietnamese | `vi` | Ukrainian            | `uk`    |
| Polish     | `pl` | Thai                 | `th`    |

> Note: Additional languages may be supported; check `deep-translator` documentation.

---

## 📁 Project Structure

```
universal_translator/
│
├── app/
│   ├── input_handlers.py      # Text, audio, and video input processing
│   ├── output_handlers.py     # Generates text, audio, and video outputs
│   ├── translator.py          # Core translation logic (deep-translator)
│
├── templates/                 # Flask HTML templates
│   └── index.html             # Main web interface
│
├── static/                    # Static assets
│   ├── css/                   # Custom styles
│   ├── js/                    # Client-side scripts
│   └── audio/                 # Translated audio files
│
├── main.py                    # CLI entry point
├── app.py                     # Flask web app entry point
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## ✅ Example

```text
Input: Hello, how are you?
Target Language: Spanish (`es`)
Output: Hola, ¿cómo estás?
[Audio plays in Spanish]
```

---

## 📌 Dependencies

- `deep-translator` – Language translation
- `gTTS` – Text-to-speech conversion
- `Flask` – Web framework
- `SpeechRecognition` – Audio input processing (beta)
- `ffmpeg-python` – Audio/video manipulation
- `moviepy` – Video processing (for future video features)

---

## 💡 License

MIT License — free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions are welcome! For major changes:
1. Open an issue to discuss your idea
2. Fork the repository and create a pull request
3. Ensure code follows PEP 8 and includes tests (if applicable)

---

## 🔮 What's Next?

- 🎙️ Full audio input support with improved accuracy
- 📹 Video input/output with subtitle and dubbing capabilities
- 🌐 Public deployment options (e.g., Render, Heroku, Fly.io)
- 🎨 Modernized UI with Tailwind CSS or Bootstrap
- ⚡ Performance optimizations for faster translations

---

Made with ❤️ by Satyendra Kumar Yadav
