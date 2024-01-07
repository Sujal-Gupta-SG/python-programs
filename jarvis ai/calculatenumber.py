import wolframalpha
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wolframalpha(query):
    apikey = "Enter api key"
    requester = wolframalpha.client(apikey)
    requested = requested.query(query)
    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")


def calc(query):
    Term = str(query)
    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "")
    Term = Term.replace("into", "")
    Term = Term.replace("minus", "")
    Term = Term.replace("plus", "")
    Term = Term.replace("divide", "")

    Final = str(Term)
    try:
        result = wolframalpha(Final)
        print(f"{result}")
        speak(result)
    except:
        speak("The result is not answerable")
