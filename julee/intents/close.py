import pyautogui
import os
from julee.intents.app_preloading import app_preloading


# def apps_close(app, apps):
def apps_close(query):
    default_apps, explorer_apps, other_apps, special_apps = app_preloading()
    app_lists = [special_apps, default_apps, other_apps]
    status = ''
    for apps in app_lists:
        keys = list(apps.keys())
        # check apps have different closing method
        if apps == special_apps:
            for app in keys:
                if app in query:
                    try:
                        status = 'Closing ' + app + '.'
                        os.system("TASKKILL /F /IM " + apps[app])
                        return status
                    except Exception as e:
                        status = e
                        return status

        # app that open and close is the same way
        else:
            for app in keys:
                if app in query:
                    try:
                        status = 'Closing ' + app + '.'
                        os.system("TASKKILL /F /IM " + apps[app] + ".exe")
                        return status
                    except Exception as e:
                        status = e
                        return status
    # if nothing execute then try close as explorer
    if status == '':
        # check apps that count as explorer.exe
        pyautogui.hotkey("ctrl", "w")
        status = 'Closing .'
        return status

def get_close(command):
    query = command.lower()
    query = query.replace("close", "")
    query = query.replace("exit", "")
    query = query.replace("stop", "")

    result = apps_close(query)
    return result
