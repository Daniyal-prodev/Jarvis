import webbrowser
import os
import platform
import subprocess
import pyautogui
import datetime
from voice_engine import speak
from ai_chat import chat_response
from scheduler import schedule_task, show_schedule
from memory import remember, recall
from utilities import get_weather, wiki_search, calculate, notify

paused = False

def open_app(name):
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.Popen(f"start {name}", shell=True)
        elif system == "Darwin":
            subprocess.Popen(["open", f"/Applications/{name}.app"])
        else:
            subprocess.Popen([name])
        speak(f"Opening {name}")
    except:
        speak("Sorry, I couldn't open the app.")

def find_and_open(target, search_type='file'):
    for root, dirs, files in os.walk("C:/"):
        if search_type == 'folder':
            if target.lower() in [d.lower() for d in dirs]:
                full_path = os.path.join(root, target)
                try:
                    os.startfile(full_path)
                    speak(f"Opening folder {target}")
                    return
                except:
                    speak("Couldn't open the folder.")
                    return
        elif search_type == 'file':
            for f in files:
                if f.lower().startswith(target.lower()):
                    full_path = os.path.join(root, f)
                    try:
                        os.startfile(full_path)
                        speak(f"Opening file {f}")
                        return
                    except:
                        speak("Couldn't open the file.")
                        return
    speak(f"No {search_type} named {target} found.")

def process_command(command):
    global paused
    command = command.lower()

    if paused and "resume" not in command:
        return
    if "pause" in command:
        paused = True
        speak("Pausing Jarvis.")
        return
    if "resume" in command:
        paused = False
    if "open tiktok" in command:
        webbrowser.open("https://tiktok.com")
        speak("Resuming Jarvis.")
        return

    if "remember" in command:
        parts = command.replace("remember", "").strip().split(" as ")
        if len(parts) == 2:
            key, value = parts
            remember(key.strip(), value.strip())
            speak(f"I'll remember {key.strip()} as {value.strip()}")
        return

    if "recall" in command:
        key = command.replace("recall", "").strip()
        value = recall(key)
        speak(value)
        return

    if "weather" in command:
        get_weather("Lahore")
        return

    if "info" in command:
        topic = command.replace("wiki", "").strip()
        wiki_search(topic)
        return

    if "calculate" in command:
        expr = command.replace("calculate", "").strip()
        calculate(expr)
        return

    if "schedule" in command:
        parts = command.replace("schedule", "").strip().split(" at ")
        if len(parts) == 2:
            task, time_str = parts
            schedule_task(task.strip(), time_str.strip())
            speak(f"Scheduled {task.strip()} at {time_str.strip()}")
        return

    if "show schedule" in command:
        show_schedule()
        return

    if "open folder" in command:
        folder = command.replace("open folder", "").strip().strip('"')
        find_and_open(folder, search_type='folder')
        return

    if "open file" in command:
        file = command.replace("open file", "").strip().strip('"')
        find_and_open(file, search_type='file')
        return

    if "open app" in command:
        app = command.replace("open app", "").strip()
        open_app(app)
        return

    if "open" in command:
        sites = {
            "google": "https://google.com",
            "youtube": "https://youtube.com",
            "facebook": "https://facebook.com",
            "instagram": "https://instagram.com"
        }
        for site in sites:
            if site in command:
                webbrowser.open(sites[site])
                speak(f"Opening {site}")
                return

    if "volume up" in command:
        pyautogui.press("volumeup")
        return
    if "volume down" in command:
        pyautogui.press("volumedown")
    if "close this tab" in command:
        pyautogui.hotkey("ctrl", "w")
        return
    if "mute" in command:
        pyautogui.press("volumemute")
        return

    if "notify" in command:
        notify("Jarvis", "This is your notification")
        return

    response = chat_response(command)
    speak(response)
