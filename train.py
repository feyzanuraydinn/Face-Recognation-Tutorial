import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()

path="images"

person_id_mapping = {}

def getImageID(path):
    faces = []
    ids = []

    for person_name in os.listdir(path):
        person_dir = os.path.join(path, person_name)
        if os.path.isdir(person_dir):
            person_id = len(person_id_mapping)
            person_id_mapping[person_name] = person_id
            for person_image in os.listdir(person_dir):
                if person_image.endswith(".jpg"):
                    person_image_path = os.path.join(person_dir, person_image)
                    faceImage = Image.open(person_image_path).convert('L')
                    faceNP = np.array(faceImage)
                    faces.append(faceNP)
                    ids.append(person_id)

    return ids, faces


IDs, facedata = getImageID(path)
recognizer.train(facedata, np.array(IDs))
recognizer.write("Trainer.yml")
cv2.destroyAllWindows()
print("Training completed.")