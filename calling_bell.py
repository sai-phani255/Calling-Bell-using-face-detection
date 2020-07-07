import cv2
import numpy as np
import os
from pygame import mixer
import time
from playsound import playsound as ps
    
mixer.init()
mixer.Sound('alarm4.wav')


def make_1080p():
    cap.set(3,1920)
    cap.set(4,1080)

sound = mixer.Sound('alarm4.wav')

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)   # to capture /read first image of the video ..0 to use the built in camera..
#make_1080p()

while(True):
    ret,frame = cap.read()
    # frame is an array which represents the image
    # ret is a bool data type returns if python is able to read the VideoCapture object
    #height,width = frame.shape[4:2] 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #cvt-convert
    
    faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.05) # to detect faces


    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y) , (x+w,y+h) , (255,0,0) , 4 )

    
        
        if(len(faces)>=1):
            sound.play()
                       
    cv2.imshow('frame',frame)
    key=cv2.waitKey(1) #this will generate a new frame after every millisecond

    if key ==ord('s'):
         break # if user enters 's'..then windows will be destroyed

cap.release() # release the camera in some milliseconds..
cv2.destroyAllWindows()  # closes all the windows

            

