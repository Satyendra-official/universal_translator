# 🌍 Universal Translator

Universal Translator is a Python-based app that can take **text, audio, or video** as input, translate it into a preferred language, and return the result as **text, speech, or even a video** with replaced or subtitled audio.

> ✅ This repo includes both a CLI tool and a basic **Flask web interface**.

---

## 📦 Features

- ✅ Translate **text input** to any language
- ✅ Convert translated text into **speech/audio**
- ✅ Web-based translator (Flask interface)
- 🛠️ Coming soon:
  - 🎙️ Voice/audio input
  - 📹 Video input (with audio extraction)
  - 🎛️ More dynamic UI/UX

---

## 🛠 Requirements

- Python 3.11 (⚠️ Python 3.12 is not recommended due to dependency issues)
- Virtual environment recommended

---

## 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/Satyendra-official/universal_translator.git
cd universal_translator
````

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

---

## 🚀 How to Use

### 🖥️ CLI Mode

```bash
python main.py
```

1. Choose input type: `text`, `audio`, or `video`
2. Enter target language code (e.g., `fr`)
3. See and hear the translation

### 🌐 Web Interface (Flask)

```bash
python app.py
```

1. Open your browser to [http://localhost:5000](http://localhost:5000)
2. Enter text and select target language
3. View and listen to the translation

---

## 🌐 Common Language Codes

| Language   | Code | Language             | Code    |
| ---------- | ---- | -------------------- | ------- |
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

---

## 📁 Project Structure

```
universal_translator/
│
├── app/
│   ├── input_handlers.py      # Handles audio/video input
│   ├── output_handlers.py     # Outputs translated text/audio
│   ├── translator.py          # Translation logic (Deep Translator)
│
├── templates/                 # Flask HTML templates
│   └── index.html
│
├── static/                    # Flask static files (audio)
│   └── translated_audio.mp3
│
├── main.py                    # CLI entry point
├── app.py                     # Flask web app entry point
├── requirements.txt
└── README.md
```

---

## ✅ Example

```text
Input: Hello, how are you?
Translated (es): Hola, ¿cómo estás?
[Audio plays in Spanish]
```

---

## 📌 Dependencies

* `deep-translator` – for language translation
* `gTTS` – text-to-speech
* `Flask` – web interface
* `SpeechRecognition`, `ffmpeg-python`, `moviepy` – for future audio/video handling

---

## 💡 License

MIT License — feel free to use, modify, and share.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss.

---

## 🔮 What's Next?

* 🎤 Audio input via web
* 📹 Translate spoken content in videos
* 💬 Upload and subtitle support
* 📲 Deploy Flask app publicly (e.g. Render, Heroku, Fly.io)

---

Made with ❤️ by Satyendra Kumar Yadav

