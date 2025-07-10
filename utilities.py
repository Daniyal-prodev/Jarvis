import requests
import wikipedia
import os
import platform
from voice_engine import speak

def get_weather(city="Lahore"):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        if response.status_code == 200:
            speak(f"The weather in {city} is {response.text}")
        else:
            speak("Couldn't fetch the weather.")
    except:
        speak("Something went wrong while getting the weather.")

def wiki_search(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)
    except:
        speak("Couldn't find that on Wikipedia.")

def calculate(expr):
    try:
        result = eval(expr)
        speak(f"The result is {result}")
    except:
        speak("I couldn't calculate that.")

def notify(title, message):
    if platform.system() == "Windows":
        from win10toast import ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=5)
