import speech_recognition as sr
import pyttsx3 as tts
import os
from dotenv import load_dotenv
from groq import Groq
import time

load_dotenv()

client = Groq(api_key = os.getenv("GROQ_API_KEY"))

EXIT_WORDS = ["exit","quit","bye","die"]

def speakText(command):

    try:
        engine = tts.init()
        engine.setProperty('voice',engine.getProperty('voices')[1].id)
        engine.setProperty('rate',175)
        time.sleep(0.5)
        engine.say(command)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("TTS ERROR: ",e)

r = sr.Recognizer()
r.energy_threshold = 300
r.dynamic_energy_threshold = True

def listen():

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.3)
        print("Listening..")

        try:
            audio = r.listen(source,timeout=5,phrase_time_limit=10)
        except sr.WaitTimeoutError:
            return ""

        try:
            text = r.recognize_google(audio).lower()
            print("You: ",text)
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

def send_to_groq(messages):

    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = messages,
        temperature=0.4,
        max_tokens = 80
    )
    message = response.choices[0].message.content.strip()
    messages.append({"role":"assistant","content":message})
    return message

messages = [
        {"role":"system",
        "content":(
            "You are Riya, a voice assistant. "
            "Keep ALL responses under 2 sentences. "
            "Never use lists or bullet points — speak in plain sentences only. "
            "Be direct and concise. "
            "When the user's request is vague or a follow-up would feel natural, end your response with a brief question. "
            "Use a friendly tone and be witty if and only when the opportunity presents itself."
        )
        }
    ]

speakText("Hi, I'm Riya. How can i help you?")

while True:

    command = listen()
    if not command:
        continue

    if any(word in command for word in EXIT_WORDS):
        print("Riya: Goodbye...")
        speakText("Goodbye")
        os._exit(0)

    messages.append({"role":"user","content":command})

    response = send_to_groq(messages)

    print("Riya: ",response)
    speakText(response)