# face_recog.py
import face_recognition
import cv2
import os
import numpy as np

KNOWN_FACES_DIR = "face_data"
TOLERANCE = 0.6

known_faces = []
known_names = []

print("Loading known faces...")
for name in os.listdir(KNOWN_FACES_DIR):
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_faces.append(encodings[0])
            known_names.append(name)

def recognize_face(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, locations)

    for face_encoding in encodings:
        matches = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
        name = "Unknown"
        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]
        return name

    return None