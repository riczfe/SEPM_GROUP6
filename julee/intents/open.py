import os
import webbrowser
from julee.intents.app_preloading import app_preloading


#still got problem when say: google chrome, google map(s), google drive
def web_check(query):
    pop_webs = ['google', 'youtube', 'facebook', 'twitter', 'reddit', 'instagram',
                'tik-tok', 'amazon', 'ebay', 'gmail', 'outlook']
    for i in pop_webs:
        if i in query:
            if i == 'tik-tok':
                i = 'tiktok'
            elif i == 'outlook':
                i = 'outlook.office'
            webbrowser.open(f"https://www.{i}.com")
            return True


def domain_check(query):
    pop_domains = ['.com', '.co', '.org', '.edu', '.net', '.io']
    for i in pop_domains:
        if i in query:
            query = query.replace(" ", "")
            webbrowser.open(f"https://www.{query}")
            return True


def drive_check(query):
    if 'drive' in query:
        list_of_words = query.split()
        driveName = list_of_words[list_of_words.index('drive') - 1]
        try:
            os.startfile(driveName + ':')
            status = 'Opening ' + driveName + ' drive.'
        except WindowsError:
            status = driveName + ' drive is not found.'
        return status
    else:
        return None


def apps_open(query):
    default_apps, explorer_apps, other_apps, special_apps = app_preloading()
    app_lists = [default_apps, explorer_apps, other_apps]
    for apps in app_lists:
        keys = list(apps.keys())
        for app in keys:
            if app in query:
                try:
                    os.startfile(apps[app])
                    status = 'Opening ' + app + '.'
                except WindowsError:
                    status = app + ' is not found or installed incorrectly on Windows.'
                return status


def get_open(command):
    query = command.lower()
    query = query.replace("open", "")
    query = query.replace("run", "")
    query = query.replace("launch", "")

    if web_check(query) is True or domain_check(query) is True:
        result = 'Opening ' + query

    elif drive_check(query) is not None:
        result = drive_check(query)

    else:
        result = apps_open(query)
    return result

"""def closeappweb(query):
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
"""