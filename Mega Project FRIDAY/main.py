import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os

# Initialize recognizer, TTS engine, and API key
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "3836f3c521cb40caa2edb167f7b45957"  # Ensure this API key is valid

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load and play the MP3 file
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Cleanup
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    # Placeholder for handling AI-specific commands
    return "I'm not sure how to handle that command."

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I could not find the song {song}.")
    elif "news" in c.lower():
        try:
            speak("Fetching the latest news...")
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                if articles:
                    speak(f"Here are the top {len(articles[:5])} headlines.")
                    for article in articles[:5]:  # Fetch the top 5 news articles
                        speak(article['title'])
                else:
                    speak("I couldn't find any news articles at the moment.")
            else:
                speak(f"Error fetching news. Status code: {r.status_code}")
        except Exception as e:
            speak(f"An error occurred: {e}")
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Friday....")
    while True:
        r = sr.Recognizer()
        print("Waiting for the wake word 'Friday'...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)  # Helps with ambient noise
                print("Listening for wake word...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)  # Shorter timeout and listening duration
            word = r.recognize_google(audio)
            print(f"Recognized: {word}")
            if word.lower() == "friday":
                speak("Yes?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Friday Active...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=4)
                    command = r.recognize_google(audio)
                    print(f"Command received: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print("Error: {0}".format(e))
