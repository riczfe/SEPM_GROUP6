import model
import os
import platform
from model.model_training import TrainingModel
import speech_recognition as sr
import pyttsx3

def read_voice_cmd(speech, self=None):
    voice_input = ''
    try:
        with sr.Microphone() as source:
            print('What do you need? I am listening...')
            audio = speech.listen(source=source, timeout=5, phrase_time_limit=5)
        voice_input = speech.recognize_google(audio)
        print('Input: {}'.format(voice_input))
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print('Network Error')
    except sr.WaitTimeoutError:
        pass
    except TimeoutError:
        pass

    return voice_input.lower()


def playsound(response, os_name):
    # Mac Execution
    if os_name == 'Darwin':
        os.system(f'say "{response}"')
    else:
        engine.say(response)
        engine.runAndWait()


if __name__ == '__main__':
    words = model.words
    classes = model.classes

    training_model = TrainingModel(words, classes, model.data_x, model.data_y)
    trained_model = training_model.train()
    # trained_model = tf.keras.models.load_model("./model/final_model.h5")

    speech = sr.Recognizer()
    engine = pyttsx3.init()
    os_name = platform.uname().system

    while True:
        command = read_voice_cmd(speech)
        # command = input("Your command: " )
        intents = training_model.get_intent(trained_model, command)
        print('Intent: ', intents)
        response = TrainingModel.get_response(intents, model.data)
        playsound(response, os_name)
