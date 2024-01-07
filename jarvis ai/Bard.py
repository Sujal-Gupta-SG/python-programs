from bardapi import BardCookies
import datetime
import pyperclip
import pyautogui
import webbrowser
from time import sleep
import json
import keyboard
import pyttsx3


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def save_cookies(cookie_dict, filename="cookies.json"):
    with open(filename, 'w') as file:
        json.dump(cookie_dict, file)


def load_cookies(filename="cookies.json"):
    try:
        with open(filename, 'r') as file:
            cookie_dict = json.load(file)
            return cookie_dict
    except FileNotFoundError:
        return None


def CookieScrapper():
    cookie_dict = load_cookies()
    if cookie_dict:
        print("Cookies loaded from file.")
        return cookie_dict

    print("*The extraction of essential cookies from GoogleBard has been accomplished successfully.")
    webbrowser.open("https://bard.google.com")
    sleep(5)
    pyautogui.click(x=1750, y=55)
    sleep(2)
    pyautogui.click(x=1573, y=251)
    sleep(2)
    pyautogui.click(x=1450, y=88)
    sleep(2)
    keyboard.press_and_release('ctrl + w')
    sleep(2)

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        print("*The process of loading cookies has been executed without any issues, and the cookies are now successfully integrated into the system.*")
        pass

    except json.JSONDecodeError as e:
        print("*Cookies Loaded Unsuccessfully*")
        print("""*The error has been identified as a result of unsuccessful cookie replication from the Chrome extension, 
which is causing a disruption in the intended functionality.*""")
        return None

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    try:
        SIDValue = next(
            (item for item in json_data if item["name"] == SID), None)
        TSValue = next(
            (item for item in json_data if item["name"] == TS), None)
        CCValue = next(
            (item for item in json_data if item["name"] == CC), None)

        if SIDValue is not None:
            SIDValue = SIDValue["value"]
        else:
            print(f"{SIDValue} not found in the JSON data.")

        if TSValue is not None:
            TSValue = TSValue["value"]
        else:
            print(f"{TSValue} not found in the JSON data.")

        if CCValue is not None:
            CCValue = CCValue["value"]
        else:
            print(f"{CCValue} not found in the JSON data.")

        cookie_dict = {
            "__Secure-1PSID": SIDValue,
            "__Secure-1PSIDTS": TSValue,
            "__Secure-1PSIDCC": CCValue,
        }

        print("")
        print(f"===> Cookie 1 - {SIDValue}")
        print(f"===> Cookie 2 - {TSValue}")
        print(f"===> Cookie 3 - {CCValue}")
        print("")

        save_cookies(cookie_dict)

        return cookie_dict

    except Exception as e:
        print(e)
        return None


def split_and_save_paragraphs(data, filename):

    try:
        paragraphs = data.split('\n\n')
        with open(filename, 'w') as file:
            file.write(data)
        data = paragraphs[:2]
        separator = ', '
        joined_string = separator.join(data)
        return joined_string
    except Exception as e:
        print(e)


def MainExecution(query):
    cookie_dict = load_cookies()

    if not cookie_dict:

        cookie_dict = CookieScrapper()

    if not cookie_dict:
        print("Cannot proceed without cookies.")
        return

    while True:
        try:
            Question = query
            RealQuestion = str(Question)
            bard = BardCookies(cookie_dict=cookie_dict)
            results = bard.get_answer(RealQuestion)['content']
            current_datetime = datetime.datetime.now()
            formatted_time = current_datetime.strftime("%H%M%S")
            filenamedate = str(formatted_time) + str(".txt")
            filenamedate = "Enter address of the file where you want to save" + filenamedate
            print(split_and_save_paragraphs(results, filename=filenamedate))
            speak(split_and_save_paragraphs(results, filename=filenamedate))

        except Exception as e:
            print(e)
        return
