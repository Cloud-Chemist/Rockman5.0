# voice_chatbot.py
import speech_recognition as sr
import pyttsx3
import openai
import os

# Set your OpenAI API key here (or via environment variable)
openai.api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here"

recognizer = sr.Recognizer()
tts = pyttsx3.init()

def get_voice_input():
    with sr.Microphone() as source:
        print("🎙 Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn’t catch that."

def respond(prompt):
    try:
        print("🧠 Thinking...")
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}]
        )
        reply = response.choices[0].message["content"].strip()
        print(f"Assistant: {reply}")
        tts.say(reply)
        tts.runAndWait()
        return reply
    except Exception as e:
        print("Error talking to OpenAI:", e)
        return "Sorry, I had trouble connecting to the assistant."
