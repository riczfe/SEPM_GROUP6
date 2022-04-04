import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import time
import requests
import wolframalpha
import pyjokes
from julee.scrape import duckduckgo_scrape_knowledge

# print('Loading your AI personal assistant - JULEE')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 195)
engine.setProperty('voice', voices[1].id)  # (depending on your default voice selector on control panel,


# normally 0 for male and 1 for female)


def speak(text):
    engine.say(text)
    engine.runAndWait()


"""
def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")
    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")
    speak("How can I help you?")
"""


def startApp(flag):
    if not flag:
        # Listen until the keyword is said
        keywords = ["julie", "julee"]
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                # r.pause_threshold = 0.8
                audio = r.listen(source)
            try:
                for i in keywords:
                    if i in r.recognize_google(audio, language='en-in').lower():
                        speak("Hi, how can I help you?")
                        print("Hi, how can I help you?")
                        return True
                        break
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 0.8
        audio = r.listen(source)

    # It takes microphone input from the user and returns string output
    try:
        print("Hang on a sec...")
        temp_query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.

    except Exception as e:
        # print(e)
        decide = random.randint(1, 2)
        if decide == 1:
            speak("Pardon me, could you say that again")
        else:
            speak("Hmm")
            speak("I'm not sure I understand.")
            speak("Can you say that again.")
        return "None"  # Say that again will be printed in case of improper voice
    return temp_query


# speak("Loading JULEE")
# wishMe()

if __name__ == "__main__":
    appCalled = startApp(False)
    while True:
        while appCalled:
                query = takeCommand().lower()  # Converting user query into lower case
                if query == 0:
                    continue

                # Logic for executing tasks based on query
                if "bye" in query or "goodbye" in query or "ok bye" in query or "stop" in query or "exit" in query:
                    speak('Ok. Good bye')
                    print('Ok. Good bye')
                    break

                if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)

                elif 'open youtube' in query:
                    webbrowser.open_new_tab("https://www.youtube.com")
                    speak("youtube is open now")
                    time.sleep(5)

                elif 'open google' in query:
                    webbrowser.open_new_tab("https://www.google.com")
                    speak("Google is open now")
                    time.sleep(5)

                elif 'open facebook' in query:
                    webbrowser.open("https://www.facebook.com")
                    speak("Facebook is open now")
                    time.sleep(5)

                elif 'play music' in query:
                    music_dir = 'C:\\Users\\Public\\Music'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    print("the time is ", {strTime})
                    speak("Sir, the time is {strTime}")

                elif 'who are you' in query or 'can you do' in query or 'what are you' in query or 'your name' in query:
                    speak('I"m JULEE, your personal assistant. I am programmed to minor tasks like '
                          'opening youtube, google chrome, gmail and stackoverflow, predict time, take a photo, search on wikipedia, predict weather'
                          'in different cities , get top headline news from times and you can ask me computational or geographical questions too!')

                elif "who made you" in query or "who created you" in query or "who discovered you" in query:
                    speak("I was created by SOFICO")
                    print("I was created by SOFICO")

                elif 'news' in query:
                    news = webbrowser.open_new_tab("https://abcnews.go.com/")
                    speak('Here are some headlines from the ABCNews, Happy reading')
                    time.sleep(6)

                #   elif 'search' in query or 'what' in query:
                #       query = query.replace("search", "")
                #       speak('Here are the results of ' + query)
                #       webbrowser.open_new_tab("https://www.google.com/search?q=" + query)
                #       time.sleep(5)

                elif 'who is' in query or 'tell me about' in query or 'what is' in query:
                    query = query.replace("who is", "")
                    query = query.replace("tell me about", "")
                    speak(duckduckgo_scrape_knowledge(query))
                    time.sleep(5)

                elif 'define' in query:
                    time.sleep(5)

                elif 'ask' in query:
                    speak('I can answer to computational and geographical questions and what question do you want to ask now')
                    question = takeCommand()
                    app_id = "R2K75H-7ELALHR35X"
                    client = wolframalpha.Client('R2K75H-7ELALHR35X')
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)

                elif "weather" in query:
                    api_key = "8ef61edcf1c576d65d836254e11ea420"
                    base_url = "https://api.openweathermap.org/data/2.5/weather?"
                    speak("whats the city name")
                    city_name = takeCommand()
                    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                    response = requests.get(complete_url)
                    x = response.json()
                    if x["cod"] != "404":
                        y = x["main"]
                        current_temperature = int(y["temp"]) - 273  # round the temperature in Kelvin, then convert to Celcius
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        speak(" It's currently " +
                              str(weather_description) +
                              "\n , with the temperature of " +
                              str(current_temperature) + "degree"
                                                         "\n and humidity in percentage is " +
                              str(current_humidiy))

                        print(" It's currently " +
                              str(weather_description) +
                              "\n , with the temperature of " +
                              str(current_temperature) + " degree"
                                                         "\n and humidity is " +
                              str(current_humidiy) + "percent.")

                    else:
                        speak("City not found? ")  # can be repeat once, if not then just exit

                elif 'joke' in query:
                    joke = pyjokes.get_joke()
                    speak(joke)
                    print(joke)

time.sleep(3)
