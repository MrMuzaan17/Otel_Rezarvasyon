import cv2
from simple_facerec import SimpleFacerec
from handd import Handetec
#from gpiozero import LED
from time import sleep

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
hnd = Handetec()
#led = LED(17)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    face_names, yes = sfr.detect_known_faces(frame)

    #cv2.imshow("Frame", frame)
    finger = hnd.all(frame)

    if int(finger) > 0 and yes == 1:
        print(finger, face_names)
        #led.on()
        print("kapı açıldı")
        sleep(5)
        #led.off()

    cv2.waitKey(3000)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
