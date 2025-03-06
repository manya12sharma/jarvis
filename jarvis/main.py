import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests 
from gtts import gTTS
import os

recognizer= sr.Recognizer()
engine= pyttsx3.init()
newsapi = "4d82558b5448424d81ff0391e4f9d522"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")  
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com") 
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1] 
        link = musiclibrary.library[song]
        webbrowser.open(link)  

    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
    # Parse JSON response
            data = r.json()

    # Extract titles
            articles= data.get('articles',[])
    
    # Print the titles
            for article in articles:
                title = article.get('title', 'No Title Found')
                print("News Title:", title)  # Debugging print
                speak(title)  # Speak the news title 
        

if __name__== "__main__":
    speak("initializing jarvis....")

    # listen for the wake word " jarvis"
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()

        print( " recognizing...")

        try:

            with sr.Microphone() as source:
                print("listening bro...")
                audio = r.listen(source,timeout=5, phrase_time_limit=4)
            word = r.recognize_google(audio)

            if ( word.lower()== "jarvis"):
                speak("ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis active..")
                    #r.adjust_for_ambient_noise(source)
                    audio = r.listen(source,timeout=5, phrase_time_limit=4)
                command = r.recognize_google(audio).lower()
                print(f"command :{command}")

                processcommand(command)

        except Exception as e :
            print( f" error ; {e}")            


    
        




