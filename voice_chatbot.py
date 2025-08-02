# voice_chatbot.py
import speech_recognition as sr
from transformers import pipeline
import pyttsx3

recognizer = sr.Recognizer()
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
tts = pyttsx3.init()

def get_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I didn’t understand."

def respond(text):
    reply = chatbot(text)[0]['generated_responses'][0]
    print(f"Bot: {reply}")
    tts.say(reply)
    tts.runAndWait()
    return reply
