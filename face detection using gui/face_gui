import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import numpy as np
import os
import subprocess


def put_moustache(mst,fc,x,y,w,h):
    
    face_width = w
    face_height = h

    mst_width = int(face_width*0.4166666)+1
    mst_height = int(face_height*0.142857)+1



    mst = cv2.resize(mst,(mst_width,mst_height))

    for i in range(int(0.62857142857*face_height),int(0.62857142857*face_height)+mst_height):
        for j in range(int(0.29166666666*face_width),int(0.29166666666*face_width)+mst_width):
            for k in range(3):
                if mst[i-int(0.62857142857*face_height)][j-int(0.29166666666*face_width)][k] <235:
                    fc[y+i][x+j][k] = mst[i-int(0.62857142857*face_height)][j-int(0.29166666666*face_width)][k]
    return fc

def put_hat(hat,fc,x,y,w,h):
    
    face_width = w
    face_height = h
    
    hat_width = face_width+1
    hat_height = int(0.35*face_height)+1
    
    hat = cv2.resize(hat,(hat_width,hat_height))
    
    for i in range(hat_height):
        for j in range(hat_width):
            for k in range(3):
                if hat[i][j][k]<235:
                    fc[y+i-int(0.25*face_height)][x+j][k] = hat[i][j][k]
    return fc

def put_dog_filter(dog,fc,x,y,w,h):
    face_width = w
    face_height = h
    
    dog = cv2.resize(dog,(int(face_width*1.5),int(face_height*1.75)))
    for i in range(int(face_height*1.75)):
        for j in range(int(face_width*1.5)):
            for k in range(3):
                if dog[i][j][k]<235:
                    fc[y+i-int(0.375*h)-1][x+j-int(0.25*w)][k] = dog[i][j][k]
    return fc
    
    
def face(x):
	
	ch=x
	cascPath = r"C:\Users\balaji\AppData\Local\Programs\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"  # for face detection

	faceCascade = cv2.CascadeClassifier(cascPath)
	log.basicConfig(filename='webcam.log',level=log.INFO)

	video_capture = cv2.VideoCapture(0)
	anterior = 0
	mst = cv2.imread('moustache.png')
	hat = cv2.imread('cowboy_hat.png')
	dog = cv2.imread('dog_filter.png')
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

			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				if ch==1:
					cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
					cv2.putText(frame,"Face Found",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2) 
				elif ch==2:
					frame = put_hat(hat,frame,x,y,w,h)
				elif ch==3:
					frame = put_moustache(mst,frame,x,y,w,h)
				elif ch==4:
					frame = put_dog_filter(dog,frame,x,y,w,h)
				else:break    
					
					
			if anterior != len(faces):
				anterior = len(faces)
				log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))
			cv2.imshow('Video', frame)


			if cv2.waitKey(1) & 0xFF == ord('x'):
				break

    

	# When everything is done, release the capture
	video_capture.release()
	cv2.destroyAllWindows()
#Creating tkinter GUI
import tkinter
from tkinter import *

def send1():
	ch=1
	face(ch)
def send2():
	ch=2
	face(ch)
def send3():
	ch=3
	face(ch)
def send4():
	ch=4
	face(ch)

root = Tk()
root.title("FACE DETECTION AND FACE FILTERS")
root.geometry("530x280")
root.resizable(width=FALSE, height=FALSE)


#Create Button to send message
faceB = Button(root, font=("Verdana",12,'bold'), text="FACE DETECTION", width="20", height=5,
                    bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
                    command= send1 )
hatB= Button(root, font=("Verdana",12,'bold'), text="HAT", width="20", height=5,
                    bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
                    command= send2)
moustacheB = Button(root, font=("Verdana",12,'bold'), text="MOUSTACHE", width="20", height=5,
                    bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
                    command= send3)
dogB = Button(root, font=("Verdana",12,'bold'), text="DOG", width="20", height=5,
                    bd=0, bg="#f9a602", activebackground="#3c9d9b",fg='#000000',
                    command= send4)

#Place all components on the screen
faceB.place(x=20, y=20, height=90)
hatB.place(x=280, y=20, height=90)
moustacheB.place(x=20, y=170, height=90)
dogB.place(x=280, y=170, height=90)

root.mainloop()
