import cv2
import numpy as np


def check(clf):
    # test start
    print("Reading image")
    test = cv2.imread('face_recognition/Face_Recognition/capture_image.jpg')
    face_cascade = cv2.CascadeClassifier("face_recognition/Face_Recognition/cascades/haarcascade_frontalface_default.xml")

    gray = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    ft = []

    for (x, y, w, h) in faces:
        roi = np.array(gray[y:y + h, x:x + w])
        roi = np.resize(roi, [150, 150])
        ft.append(roi)

    ft = np.array(ft)

    try:
        # 3d array to 2d array
        nsamp, nx, ny = ft.shape
        d2_test_dataset = ft.reshape((nsamp, nx * ny))

        prediction_face = clf.predict(d2_test_dataset)
        print("Face: ", prediction_face)

        prediction_face = prediction_face[0]

        if prediction_face == 0:
            print("Dipesh")
        elif prediction_face == 1:
            print("Gayyur")
        elif prediction_face == 2:
            print("Rubal")
        elif prediction_face == 2:
            print("Totlaney")
        else:
            print("Dont' know")
    except:
        print("Face not found")
