import cv2
import os

name = input("Enter name (folder must exist in face_data): ")
folder = f"face_data/{name}"
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Press 's' to save, 'q' to quit", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        filename = os.path.join(folder, f"{name}_{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
