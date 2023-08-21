"""
Uses cv2 video capturing and cvzone HandTracking module to detect how many fingers someone holds up
to turn on that many LEDs connected to an Arduino
"""

import cv2
from cvzone.HandTrackingModule import HandDetector
import controller as cnt

#video with 0.8 detection confidence
detector = HandDetector(0.8, 1)

video = cv2.VideoCapture(0)

while True:
    #read frames of video
    ret, frame=video.read()
    #flip frame
    frame=cv2.flip(frame,1)
    #get hand and its "landmarks"
    hands, img = detector.findHands(frame)

    if hands:
        #get first hand detected
        lmList = hands[0]
        #returns list of integers representing which fingers are up
        fingerUp = detector.fingersUp(lmList)

        # print(fingerUp)

        cnt.led(fingerUp)

        #turn on LEDs according to finger list
        fingers_list = ["thumb", "pointer", "middle", "ring", "pinky"]
        print_str = "Fingers up: "
        for idx, x in enumerate(fingerUp):
            if x == 1:
                print_str += fingers_list[idx] + " "

        cv2.putText(frame, print_str, (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)

    #display frame
    cv2.imshow("frame",frame)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cnt.led([0,0,0,0,0]) #turn off all LEDs on quit
video.release()
cv2.destroyAllWindows()