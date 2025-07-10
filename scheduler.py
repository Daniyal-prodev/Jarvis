import schedule
import time
from threading import Thread
from voice_engine import speak

tasks = []

def schedule_task(task, time_str):
    def job():
        speak(f"Reminder: {task}")
    schedule.every().day.at(time_str).do(job)
    tasks.append((task, time_str))

def show_schedule():
    if not tasks:
        speak("No tasks scheduled.")
    for task, time_str in tasks:
        speak(f"{task} at {time_str}")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

Thread(target=run_scheduler, daemon=True).start()
