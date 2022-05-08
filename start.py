import speech_recognition as sr
import os
import pygame
import playsound
from gtts import gTTS
from pathlib import Path  # for directory listing
import tensorflow as tf

import model
from model.model_training import TrainingModel

from julee.intents.joke import get_joke
from julee.intents.knowledge_scrape import google_search
from julee.intents.news import open_news
from julee.intents.time import get_time
from julee.intents.weather import get_weather
from julee.intents.wikipedia import get_wikipedia
from julee.intents.open import get_open
from julee.intents.close import get_close
from julee.control.main import control_mode
from julee.control.others import fullscreen_mode

# using gTTS to read text
def speak(text):
    # print(text)
    text_to_speech = gTTS(text=text, lang='en')
    filename = "temp.mp3"  # bypass saving a mp3 file of answering
    text_to_speech.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


# play activate sound
def activate():
    path = Path(__file__).parent / "./data/sound/activate.mp3"
    play_sound(path)


# play finish sound
def finish():
    path = Path(__file__).parent / "./data/sound/finish.mp3"
    play_sound(path)


# using pygame to play sound
def play_sound(path):
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(path)
    sound.play()


def read_voice_cmd():
    speech = sr.Recognizer()
    voice_input = ''
    try:
        with sr.Microphone() as source:
            print("Waiting for any commands...")
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


# loading trained model for prediction
def load_model():
    words = model.words
    classes = model.classes

    training_model_temp = TrainingModel(words, classes, model.data_x, model.data_y)
    trained_model_temp = tf.keras.models.load_model("./model/final_model.h5")
    return training_model_temp, trained_model_temp


# remove to avoid error from the answer
def preprocess_command(preprocess_input):
    command_preprocess = preprocess_input.lower()
    command_preprocess = command_preprocess.replace("can you", "")
    command_preprocess = command_preprocess.replace("could you", "")
    command_preprocess = command_preprocess.replace("may you", "")
    command_preprocess = command_preprocess.replace("might you", "")
    command_preprocess = command_preprocess.replace("will you", "")
    command_preprocess = command_preprocess.replace("would you", "")
    command_preprocess = command_preprocess.replace("can you", "")
    command_preprocess = command_preprocess.replace("please", "")
    return command_preprocess


def intents_load(command_intent, intent, response):
    simples = ["greeting", "alt_greet", "simple_question", "bye", "introduction", "skill", "misunderstanding"]
    for i in simples:
        if intent == i:
            result = response
            if intent == 'skill':
                print('https://github.com/riczfe/SEPM_GROUP6')
            return result

    if intent == 'joke':
        result = get_joke()
        return result

    elif intent == 'news':
        open_news()
        result = response
        return result

    elif intent == 'time':
        result = get_time()
        return result

    elif intent == 'weather':
        speak("What's the city name?")
        activate()
        city_name = read_voice_cmd()
        finish()
        if city_name or city_name != "":
            result = get_weather(city_name)
        # if did not say city then just drop the weather function(but needed to implement to GUI)
        else:
            result = 'Cancel searching.'
        return result

    elif intent == 'google_search':
        result = google_search(command_intent)
        if result is not None:
            print(result)
            return 'Here are some information.'
        else:
            result = 'Cancel searching.'
            return result

    elif intent == 'wikipedia':
        result = get_wikipedia(command_intent)
        return result

    elif intent == 'control_open':
        result = get_open(command_intent)
        return result

    elif intent == 'control_close':
        result = get_close(command_intent)
        return result

    elif intent == 'control_mode':
        control_mode()
        return ""

    elif intent == 'win_placement':
        fullscreen_mode()
        return ""


if __name__ == '__main__':
    training_model, trained_model = load_model()
    while True:
        flag = False
        call = read_voice_cmd()
        if auto_recognize(call, flag) is True:
            activate()
            print("Listening...")
            query = read_voice_cmd()
            command = preprocess_command(query)
            if command or command != "":
                finish()
                try:
                    intents = training_model.get_intent(trained_model, command)
                    print('Intent: ', intents)
                    responses = TrainingModel.get_response(intents, model.data)
                    final_result = intents_load(command, intents[0], responses)
                except Exception as e:
                    print(e)
                    final_result = ''
                """
                USE final_result FOR DISPLAY OUTPUT ONLY, NO CONFIGURATION.
                """
                print("Answer: " + final_result)
                try:
                    speak(final_result)
                except AssertionError:
                    print("Cancel command.")
