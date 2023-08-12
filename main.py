"""
Uses cv2 video capturing and cvzone HandTracking module to detect how many fingers someone holds up
to turn on that many LEDs connected to an Arduino
"""

import cv2
#cvzone uses OpenCV and mediapipe libraries
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

# #detectionCon=0.8, maxHands=1 --> video with 0.8 detection confidence
detector=HandDetector(0.8, 1)

video=cv2.VideoCapture(0)

while True:
    #read frames of video
    ret, frame=video.read()
    #flip frame
    frame=cv2.flip(frame,1)
    #get hand and its "landmarks"
    hands, img=detector.findHands(frame)

    if hands:
        #get first hand detected
        lmList=hands[0]
        #automatically finds how many fingers are up and returns list of integers
        fingerUp=detector.fingersUp(lmList)

        # print(fingerUp)
        #turn on LEDS equal to number of fingers up

        # cnt.led(fingerUp)

        #TODO- make this more efficient once connect to arduino
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Finger count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'Finger count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'Finger count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Finger count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)

    #display frame
    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==ord("k"):
        break

video.release()
cv2.destroyAllWindows()