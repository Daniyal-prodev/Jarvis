import speech_recognition as sr
import time
import threading
from voice_engine import speak
from commands import process_command

recognizer = sr.Recognizer()
def listen_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {command}")
            return command
        except:
            return ""

if __name__ == "__main__":
    speak("hey i am jarvis how can i help you.")
    speak("Please enter the required information its my policy to know you:")
    name=input("Enter your name: ")
    birthdate=input("Enter your birthdate: ")
    age=input("Enter your age: ")
    father_name=input("Enter your father's name: ")
    school_name=input("Enter your school name: ")
    brother_name=input("Enter your brother's name: ")
    birthplace=input("Enter your birthplace: ")
    adress=input("Enter your address: ")
    birthdate=input("Enter your birthdate: ")
    speak(f"Nice to meet you {name}, I will remember your birthdate is {birthdate}.")
    while True:
        cmd = listen_command()
        if cmd:
            process_command(cmd)
