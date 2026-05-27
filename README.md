# Riya — Voice Assistant

A conversational voice assistant that listens through your microphone, thinks with **LLaMA 3.1 8B** via Groq, and talks back using text-to-speech.

## Features

- Wake-free continuous listening
- Natural multi-turn conversation with full message history
- Text-to-speech responses (female voice, tuned rate)
- Ambient noise adjustment for cleaner recognition
- Graceful exit on voice commands (`exit`, `quit`, `bye`, `die`)

## Requirements

```
groq
python-dotenv
speechrecognition
pyttsx3
pyaudio
```

```bash
pip install groq python-dotenv speechrecognition pyttsx3 pyaudio
```

> On Windows, if `pyaudio` fails: `pip install pipwin` then `pipwin install pyaudio`

## Setup

1. Clone the repo
2. Create a `.env` file:
   ```
   GROQ_API_KEY=your_api_key_here
   ```
3. Make sure your microphone is connected and set as default

## Usage

```bash
python main.py
```

Riya will greet you and start listening. Just speak — no wake word needed.

Say `exit`, `quit`, or `bye` to stop.

## Notes

- Requires an internet connection for both Google Speech Recognition and Groq
- Response length is capped at 80 tokens to keep replies short and natural
- TTS voice defaults to the second available system voice — change the index in `speakText()` if needed
