import cv2
import pathlib
import numpy as np

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
print(cascade_path)



def main():
    print("Hello world!")

    face_classifier = cv2.CascadeClassifier(str(cascade_path))

    capture_device = cv2.VideoCapture(0)

    while True:
        ret, frame = capture_device.read()

        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        detected_faces = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        for (x,y,width,height) in detected_faces:
            cv2.rectangle(frame, (x,y),(x+width,y+height),(255,255,0),2)

        cv2.imshow('Real Time Video', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    capture_device.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()