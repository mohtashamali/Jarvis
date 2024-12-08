import pyttsx3 #used by the machine to speak[speaker]
import datetime #it will import time
import pyaudio # ectension for microphone in python{microphone-}
import speech_recognition as sr # basically a microphone
import wikipedia # you know it 
from googlesearch import search
import webbrowser
import os # you know it I know it 
import  subprocess # you know it I know it 
# import whether
# import android
# -----------------------------------------

datime = datetime
eng = pyttsx3.init('sapi5')
voices = eng.getProperty('voices')
eng.setProperty('voice', voices[1].id)

# Function to make the assistant speak--
def speak(audio):
    eng.say(audio)
    eng.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Jarvis is listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Boss said: {query}\n")
        return query
    except Exception as e:
        print("Could not understand audio, please say that again.")
        return "None"

# Function to search Google and return top 3 results
def google_search(query):
    speak("Searching is going on ")
    search_results = search(query, num_results=3)  # Limit to top 3 results
    return search_results


if __name__ == "__main__":
    speak("Hey boss, how can I help you?")
    while True:
        query = listen().lower()
        feel=listen().lower()

        # Check if Wikipedia is mentioned in the query
        if 'wikipedia' in query:
            speak("Searching is going on ")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Check if Google search is mentioned in the query
        elif 'hi' in query:
                speak("hello how are you doing")
        elif  'googlesearch' in query:
                speak("google Searching is going on")
                query = query.replace("search", "").replace("google", "")
                search_results = google_search(query)
                for result in search_results:
                    speak("Here are some link ")
                    print(result)
        elif 'google' in query:
                speak("opening Google")
                webbrowser.open("google.com")
        elif 'facebook' in query:
                speak("opening facebook")
                webbrowser.open("facebook.com")
        elif 'instagram' in query:
                speak("opening instagram")
                webbrowser.open("instagram.com")       
        elif 'youtube' in query:
                speak("Opening youtube")
                webbrowser.open("youtube.com")
        elif 'lords'  in query:
                speak(" medical college for more detail see here You can go for it here ")
                webbrowser.open('https://www.lords.ac.in/')
        elif 'mail' in query:
                speak("Opening mail")
                webbrowser.open("mail.com")    
        elif 'whatsapp' in query:
                speak("Opening mail")
                webbrowser.open("whatsapp.com") 
        elif 'calculator' in query:
            speak("opening calculator")
            calculator_path = 'C:\\Windows\\System32\\calc.exe'
            subprocess.Popen([calculator_path])
        elif 'time' in query:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(strTime)
        if 'bye' in query or 'stop' in query or 'leave' in query or 'Tata ' in query or 'die' in query :
                speak("GoodByye boss! ")
                break
       
                