import speech_recognition as sr
from pathlib import Path  # for directory listing
import pygame
import playsound


def read_voice_cmd():
    speech = sr.Recognizer()
    voice_input = ''
    try:
        with sr.Microphone() as source:
            print("Wait for waking up.")
            audio = speech.listen(source=source, timeout=5, phrase_time_limit=5)
        # recognize speech using Google Speech Recognition
        voice_input = speech.recognize_google(audio, language='en')
        print('Input: {}'.format(voice_input))
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.WaitTimeoutError:
        pass
    except TimeoutError:
        pass
    return voice_input.lower()


# play activate sound
def activate():
    path = Path(__file__).parent / "./data/sound/activate.mp3"
    play_sound(path)


# using pygame to play sound
def play_sound(path):
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(path)
    sound.play()


# listening until julee is called
def auto_recognize(command_rec, flag):
    # it is impossible to know the word "julee", so have to put the word with similar sound
    keywords = ["julie", "julee", "yulee", "yulie", "jewelry", "jule",
                "julia", "juli", "julio", "julay", "juley", "julery",
                "jullie", "jully", "julet", "juli", "rulie", "jolie", "jolee",
                "guillie", "julien", "juni"]

    # check if keyword appear
    for i in keywords:
        if i in command_rec:
            flag = True
            break
    return flag


if __name__ == '__main__':
    while True:
        flag = False
        call = read_voice_cmd()
        ######################################################################
        # for debug, comment the above code and remove comment the code below
        # call = input("command:")
        ######################################################################
        if auto_recognize(call, flag) is True:
            # activate()
            # for python
            # exec(open("takecommand.py").read())
            exec(open("src/main/takecommand.py").read())
