import speech_recognition as sr
import pyttsx3  #pip install pyttsx3
import datetime  #module
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os  #inbuilt
import requests, json  #inbuilt

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("hi sir, Good Morning!")
    elif (hour >= 12 and hour < 18):
        speak("hi sir, Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("hi sir, Good Evening")
    else:
        speak("hi sir,Goodnight")
    speak("Good to see you again")
    speak("Jarvis at your service, Please tell me how can i help you?")
r = sr.Recognizer()
def cmdusr():
	with sr.Microphone() as source:
		try:
			r.adjust_for_ambient_noise(source)
			print("Listening sir")
			speak("listening sir")
			data = r.record(source, duration=3)
			text = r.recognize_google(data)
			print(text)
		except Exception as e:
			print(e)
			speak("Say that again please...")
			cmdusr()
wishme()
cmdusr()
