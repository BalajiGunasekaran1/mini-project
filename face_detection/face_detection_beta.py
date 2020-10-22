import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import numpy as np
import os
import subprocess


cascPath = r"C:\Users\balaji\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"  # for face detection

faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
		if not video_capture.isOpened():
			print('Unable to load camera.')
			sleep(5)
			pass

		# Capture frame-by-frame
		ret, frame = video_capture.read()

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(40,40)
		)
		for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
				cv2.putText(frame,"Face Found",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2) 
				
		if anterior != len(faces):
				anterior = len(faces)
				log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))
		cv2.imshow('Video', frame)


		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

    

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
