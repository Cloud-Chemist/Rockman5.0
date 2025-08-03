# assistant.py
import cv2
from face_recognition import recognize_face
from voice_chatbot import get_voice_input, respond
from youtube_player import play_youtube

cap = cv2.VideoCapture(0)
print("Starting AI Assistant...")

# Greet when face is recognized
name = "Unknown"
while True:
    ret, frame = cap.read()
    if not ret:
        continue

    name = recognize_face(frame)
    if name and name != "Unknown":
        print(f"Hello, {name.capitalize()}!")
        respond(f"Hello, {name}. How can I help you today?")
        break

cap.release()

# Voice interaction loop
while True:
    command = get_voice_input().lower()

    if "play" in command and "youtube" in command:
        respond("What do you want me to play?")
        query = get_voice_input()
        respond(f"Playing {query} on YouTube")
        play_youtube(query)

    elif "exit" in command or "goodbye" in command:
        respond("Goodbye!")
        break

    else:

        respond(command)
