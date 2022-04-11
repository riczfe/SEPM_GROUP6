import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp = {"command prompt": "cmd", "control panel": "control", "resource monitor": "resmon",
           "device manager": "devmgmt.msc", "disk management": "diskmgmt.msc", "task manager": "taskmgr",
           "paint": "mspaint", "word": "winword", "excel": "excel", "powerpoint": "powerpnt",
           "this pc": "explorer", "file explorer": "explorer", "my folder": ".",
           "chrome": "chrome", "firefox": "firefox", "edge": "msedge",
           "vscode": "code", "calculator": "calc", "notepad": "notepad",
           "keyboard": "osk", "mouse setting": "main.cpl"}


def openappweb(query):
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("julie", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")

    # this way to open drive without checking what drives the user might have
    elif 'drive' in query:
        list_of_words = query.split()
        driveName = list_of_words[list_of_words.index('drive') - 1]
        os.system(f"start {driveName}:")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                speak("Launching, sir")
                os.system(f"start {dictapp[app]}")
                break


def closeappweb(query):
    speak("Closing,")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
