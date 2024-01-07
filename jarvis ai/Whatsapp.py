import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said :{query}\n")
    except:
        print("Say That again")
        return "None"
    return query


strtime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes=2)).strftime("%M"))


def sendMessages():
    speak("who do you want to message")
    a = int(input('''1.)person\n2.)person2 \n3.)person3 \nEnter your input :  '''))
    if a == 1:
        speak("whats the message")
        message = str(input("Enter the message - "))
        pywhatkit.sendwhatmsg("+919999999999", message,
                              time_hour=strtime, time_min=update)
    elif a == 2:
        speak("whats the message")
        message = str(input("Enter the message - "))
        pywhatkit.sendwhatmsg("+919999999999", message,
                              time_hour=strtime, time_min=update)
    elif a == 3:
        speak("whats the message")
        message = str(input("Enter the message - "))
        pywhatkit.sendwhatmsg("+919999999999", message,
                              time_hour=strtime, time_min=update)
