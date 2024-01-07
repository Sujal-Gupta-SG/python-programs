import requests
import json
import pyttsx3


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# get api key from here https://newsapi.org/


def latestnews():
    apidict = {"value:key"}
    content = None
    url = None
    speak(
        "which field news do you want ,[latest india news],[bussiness],[entertainment],[health],[science],[sports],[technology]")
    field = input("Type field News that you want:")
    for key, value in apidict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("Url was found")
            break
        else:
            url = True
    if url is True:
        print("URl NOt FOUND")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit :{news_url}")
        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("That's all")
