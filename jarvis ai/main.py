import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
from plyer import notification
from pygame import mixer
import speedtest


for i in range(3):
    a = input("Enter Password to open Jarvis:-")
    pw_file = open("rem.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("WELCOME BOSS ! PLEASE SPEAK [WAKE UP JARVIS] TO LOAD ME UP")
        break
    elif (i == 2 and a != pw):
        exit()
    elif (a != pw):
        print("TRY AGAIN")


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)
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


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


asking_list = ["what is", "tell me about", "explain", "how does", "why is", "can you", "give me details on", "describe", "define", "help me understand", "provide information about", "list", "compare", "contrast", "solve", "calculate",
               "recommend", "suggest", "what are the benefits of", "what are the risks of", "how can I", "what are some tips for", "where can I find", "when was", "who is", "where is", "is it possible to", "can you explain the process of", "how do I"]


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up " in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak(" Ok Boss , You can Wake up me anytime")
                    break

################## Jarvis 2. o #######################
                elif any(query.startswith(phrase) for phrase in asking_list):
                    from Bard import MainExecution
                    query = query.replace("jarvis", "")
                    MainExecution(query)
                elif "jarvis change your password" in query:
                    speak("what's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("rem.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done Boss")

                elif "jarvis schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i+1}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i+1}. {tasks[i]}\n")
                            file.close()
                elif "jarvis show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )
                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576  # Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ", download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")
                elif "screenshot" in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                elif "focus mode" in query:
                    a = int(input(
                        "Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a == 1):
                        speak("Entering the focus mode....")
                        os.startfile(
                            "Enter the focus mode file address here\\FocusMode.py")
                        exit()
                    else:
                        pass

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis", "")
                    query = query.replace("translate", "")
                    translategl(query)


###############################################################################################################################################################
                elif "hello" in query:
                    speak("Hello Boss , How are you ?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("Perfect Boss")
                elif "thank you" in query:
                    speak("you are welcome, Boss")
                elif "pause the video" in query:
                    pyautogui.press("k")
                elif "play the video" in query:
                    pyautogui.press("k")
                elif "mute the video" in query:
                    pyautogui.press("m")
                    speak("video Muted")
                elif "forward ten seconds" in query:
                    pyautogui.press("l")
                elif "back ten seconds" in query:
                    pyautogui.press("j")
                elif "forward five seconds" in query:
                    pyautogui.press(">")
                elif "back five seconds" in query:
                    pyautogui.press("<")
                elif "volume up" in query:
                    from keyboard import volumeup
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    volumedown()
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "google" in query:
                    from SearchNow import seachGoogle
                    seachGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "news" in query:
                    from Newsread import latestnews
                    latestnews()
                elif "calculate" in query:
                    from calculatenumber import wolframalpha
                    from calculatenumber import calc
                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    calc(query)
                elif "send a whatsapp" in query:
                    from Whatsapp import sendMessages
                    sendMessages()
                elif "temperature" in query:
                    search = "current temperature"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current temperature is {temp}")
                elif "weather" in query:
                    search = "current weather"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current weather is {temp}")
                elif "set an alarm" in query:
                    print("Input Time Example :-10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please Tell me The Time:- ")
                    alarm(a)
                    speak("Done, BOSE")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Boss , the time is {strTime}")
                elif "close your program" in query:
                    speak("Doing fully close my program ")
                    exit()
                elif "jarvis remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    rememberMessage = query.replace("i", "you")
                    speak("You told me " + rememberMessage)
                    remember = open("remember.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt", "r")
                    speak("You told me  " + remember.read())
                elif "jarvis shutdown the system" in query:
                    speak("Are you sure you want to shutdown")
                    shutdown = input(
                        "Do you wish to shutdown your system?(y/n)")
                    if shutdown == "y":
                        os.system("shutdown /s /t 1")
                    else:
                        break

                else:
                    # For all other queries
                    from Bard import MainExecution
                    query = query.replace("jarvis", "")
                    MainExecution(query)
