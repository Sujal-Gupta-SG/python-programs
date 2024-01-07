import pyttsx3
import datetime
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


extractedtime = open("Alarmtext.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alartext.txt", "r+")
deletetime.truncate(0)
deletetime.close()


def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis", "")
    timenow = timenow.replace("set an alarm", "")
    timenow = timenow.replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            os.system("Enter music address here")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()


ring(time)
