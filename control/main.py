import speech_recognition as sr
import pyautogui
import os


def read_voice_cmd():
    speech = sr.Recognizer()
    voice_input = ''
    try:
        with sr.Microphone() as source:
            print("Waiting for any commands...")
            audio = speech.listen(source=source, timeout=5, phrase_time_limit=5)
        # recognize speech using Google Speech Recognition
        voice_input = speech.recognize_google(audio, language='en')
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.WaitTimeoutError:
        pass
    except TimeoutError:
        pass
    print('Input: ' + voice_input)
    return voice_input


def text_dict():
    pyautogui.hotkey("win", "h")


def preloading():
    print("Speech control activate")
    os.system("start /min /B %windir%\Speech\Common\sapisvr.exe -SpeechUX")


def speech_dict():
    pyautogui.hotkey("ctrl", "win")


def control_mode():
    preloading()
    while True:
        result = read_voice_cmd()
        if "stop dictating" in result or "stop detecting" in result or "stop typing" in result:
            print("Text detecting stopped")
            text_dict()

        elif "start dictating" in result or "start detecting" in result or "start typing" in result:
            print("Text detecting started")
            text_dict()

        elif "start listening" in result or "start control" in result:
            speech_dict()

        elif "exit control mode" in result or "exit voice control" in result or "exit smart control" in result:
            os.system("taskkill /f /im sapisvr.exe")
            break

