import pyttsx3
import datetime


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetMe():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print(f"Welcome Boss, Good morning ")
        speak(f"Welcome Boss, Good morning ")
    elif hour >= 12 and hour < 17:

        print(f"Welcome Boss, Good Afternoon ")

        speak(f"Welcome Boss, Good Afternoon ")
    elif hour >= 17 and hour < 21:
        print(f"Welcome Boss, Good Evening ")
        speak(f"Welcome Boss, Good Evening ")
    else:

        print(f"Welcome BOSS, Now the time is for Sleep Boss.You want to work tonight today ,Boss ?")

        speak(f"Welcome BOSS, Now the time is for Sleep Boss.You want to work tonight today ,Boss ?")
