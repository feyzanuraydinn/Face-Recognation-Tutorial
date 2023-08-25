import cv2
import os

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("Trainer.yml")

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
        if conf < 50:
            person_names = os.listdir("images")
            person_name = person_names[serial]
            color = (0, 255, 0)
            text_color = (255, 255, 255)
        else:
            person_name = "Unknown"
            color = (0, 0, 255)
            text_color = (255, 255, 255)
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.rectangle(frame, (x, y-40), (x+w, y), color, -1)
        cv2.putText(frame, person_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, text_color, 2)
    
    cv2.imshow("Frame", frame)
    
    k = cv2.waitKey(1)
    
    if k == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
