import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# THIS VERSION OF THIS SOFTWARE ONLY 
# SUPPORTS ON PYTHON v3.6.9 or lower

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning !')

    elif hour>=12 and hour<18:
        speak('Good Afternoon !')

    else:
        speak('Good Evening !')
    
    speak('How may I help you ?')

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes I am listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
            print("Hang on a sec...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"You said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    

        print("I'm sorry couldn't quiet get that. Please try again...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results) 
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Public\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  
            print("the time is ",{strTime})  
            speak(f"Sir, the time is {strTime}")
            
        else:
            break
        