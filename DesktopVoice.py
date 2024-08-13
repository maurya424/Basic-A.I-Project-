import time
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import numpy as np
import sounddevice as sd
import urllib.parse


from scipy.io import wavfile

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    print("The current time is ", Time)

def get_date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is " + str(day) + "/" + str(month) + "/" + str(year))

def wish_me():
    print("Welcome to AI")
    speak("Welcome to AI")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning buddy")
        print("Good Morning buddy")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon buddy")
        print("Good Afternoon buddy")
    elif hour >= 16 and hour < 24:
        speak("Good Evening buddy")
        print("Good Evening buddy")
    else:
        print("Take rest in your life buddy ")
        speak("Take rest in your life buddy ")
    
    print("Tell me how may I help you.")
    speak("Tell me how may I help you.")

def take_screenshot(file_path):
    img = pyautogui.screenshot()
    img.save(file_path)

def detect_snap_sound(duration=2, threshold=3000):
    print("Wake up sound ...")
    fs = 44100  # Sample rate
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished

    amplitude = np.max(np.abs(recording))
    if amplitude > threshold:
        print("Sound detected!")
        return True

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8  # Adjust this value as needed
        r.non_speaking_duration = 0.5  # Adjust this value as needed
        r.adjust_for_ambient_noise(source, duration=0.5) 
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        print(query)

    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that. Please type your command.")
        query = input("Type your command: ")

    return query.lower()


if __name__ == "__main__":
    wish_me()
    while True:
        if detect_snap_sound():
            pass
            query = take_command()

            if "time" in query:
                get_time()

            elif "date" in query:
                get_date()

            elif "who are you" in query:
                speak("I'm AI created by Sumit Maurya and his group. I'm a beginner desktop voice assistant.")
                print("I'm AI created by Sumit Maurya and his group. I'm a beginner desktop voice assistant.")

            elif "how are you" in query:
                speak("I'm fine buddy, What about you?")
                print("I'm fine buddy, What about you?")

            elif "fine" in query:
                speak("Glad to hear that bro")
                print("Glad to hear that bro")

            elif "thanks" in query:
                speak("Never mind bro")
                print("Never mind bro")

            elif "good" in query:
                speak("Glad to hear that bro")
                print("Glad to hear that bro")

            elif "wikipedia" in query:
                try:
                    speak("Ok wait sir, I'm searching...")
                    query = query.replace("wikipedia", "")
                    result = wikipedia.summary(query, sentences=2)
                    print(result)
                    speak(result)
                except:
                    speak("Can't find this page sir, please ask something else")

            elif "open youtube" in query:
                speak("Opening YouTube")
                print("Opening YouTube")
                wb.open("youtube.com") 

            elif "open google" in query:
                speak("Opening Google")
                print("Opening Google")
                wb.open("google.com") 

            elif "open stack overflow" in query:
                speak("Opening Stack Overflow")
                print("Opening Stack Overflow")
                wb.open("stackoverflow.com")

            elif "play music" in query:
                speak("Playing music")
                print("Playing music")
                song_dir = os.path.expanduser("C:\\Users\\Lenovo\\OneDrive\\Music\\relif")
                songs = os.listdir(song_dir)
                print(songs)
                x = len(songs)
                y = random.randint(0, x-1)
                os.startfile(os.path.join(song_dir, songs[y]))

            elif "open setting" in query:
                speak("Opening setting")
                print("Opening setting")
                settings_path = "C:\\Windows\\System32\\control.exe"
                os.startfile(settings_path)

            elif "open mail" in query:
                speak("Opening mail")
                print("Opening mail")
                wb.open("gmail.com")

            elif "open edge" in query: 
                speak("Opening Edge")
                print("Opening Edge")
                edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(edge_path) 

            elif "open brave" in query: 
                speak("Opening Brave")
                print("Opening Brave")
                brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                os.startfile(brave_path) 

            elif "search on edge" in query:
                try:
                    speak("What should I search?")
                    print("What should I search?")
                    search = take_command() 
                    print(f"Opening new tab with search query: {search}")
                    
                    encoded_search = urllib.parse.quote(search)
                    
                    search_url = f"https://www.bing.com/search?q={encoded_search}"
                    
                    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    wb.register('edge', None, wb.BackgroundBrowser(edge_path))
                    wb.get('edge').open_new_tab(search_url)
                    
                    print("Search query opened successfully.")
                except Exception as e:
                    print("Error opening search query:", e)
                    speak("Can't open now, please try again later.")
                    print("Can't open now, please try again later.")
                        

            elif "remember that" in query:
                speak("What should I remember")
                print("What should I remember")
                data = take_command()
                speak("You said me to remember that " + data)
                print("You said me to remember that " + str(data))
                with open("data.txt", "w") as remember:
                    remember.write(data)

            elif "do you remember anything" in query:
                try:
                    with open("data.txt", "r") as remember:
                        data = remember.read()
                        print("You told me to remember that " + data)
                        speak("You told me to remember that " + data)
                except FileNotFoundError:
                    speak("I don't have anything to remember.")

            elif "screenshot" in query:
                print("Taking screenshot")
                speak("Taking screenshot")
                timestamp = time.strftime("%Y%m%d-%H%M%S")
                file_path = f"C:\\Users\\Lenovo\\OneDrive\\One_Drive_Storage\\OneDrive\\Pictures\\Screenshots_{timestamp}.png"
                take_screenshot(file_path)
                print("Done, please check it")
                speak("Done, please check it")

            elif "offline" in query:
                print("Ok bye-bye buddy")
                speak("Ok bye-bye buddy")
                quit()

            elif "shut down" in query:
                speak("Shutting down")
                print("Shutting down")
                os.system("shutdown /s /t 10")
