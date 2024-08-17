"""
    Name: Saeed Mahmadzuber Ghasura
    Project: Voice Assistant
"""

import speech_recognition as sr
import pyttsx3
import requests
import subprocess
from datetime import datetime

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def get_default_microphone_index():
    default_index = 0
    return default_index

def listen():
    mic_index = get_default_microphone_index()
    
    try:
        with sr.Microphone(device_index=mic_index) as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source) 
            audio = recognizer.listen(source)
            
            if audio is None:
                speak("I didn't catch that. Could you please repeat?")
                return ""
            
            try:
                text = recognizer.recognize_google(audio)
                print(f"You said: {text}")
                return text.lower()
            except sr.UnknownValueError:
                speak("Sorry, I did not understand that.")
                return ""
            except sr.RequestError:
                speak("Could not request results from the service.")
                return ""
    except sr.WaitTimeoutError:
        speak("Timeout listening. Please try again.")
        return ""
    except Exception as e:
        speak(f"Error accessing the microphone: {str(e)}")
        return ""

def get_weather():
    api_key = "eea4d49d67b16c4f1ab04a2fd9dc3efb" 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Ahmedabad"  
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        weather_description = data["weather"][0]["description"]
        speak(f"The temperature in {city_name} is {temperature} degrees Celsius with {weather_description}.")
    else:
        speak("City not found.")

def open_notepad():
    speak("Opening Notepad.")
    return subprocess.Popen(["notepad.exe"])

def close_notepad(process):
    if process:
        speak("Closing Notepad.")
        process.terminate()

def get_current_time():
    current_time = datetime.now().strftime("%I:%M %p")  
    speak(f"The current time is {current_time}.")

def main():
    commands = [
        "stop", "goodbye", "exit", 
        "hello", "how are you", 
        "get weather", "what is the weather today", 
        "open notepad", 
        "close notepad", 
        "current time", "time"
    ]
    
    print("Available commands:")
    for command in commands:
        print(f"- {command}")
    
    speak("Hello! How can I assist you today?")
    notepad_process = None
    
    while True:
        command = listen()
        if command:
            if "stop" in command or "goodbye" in command or "exit" in command:
                speak("Goodbye!")
                close_notepad(notepad_process)
                break
            elif "hello" in command or "how are you" in command:
                speak("Hello! I'm doing well, thank you.")
            elif "get weather" in command or "what is the weather today" in command:
                get_weather()
            elif "open notepad" in command:
                if notepad_process is None:
                    notepad_process = open_notepad()
                else:
                    speak("Notepad is already open.")
            elif "close notepad" in command:
                close_notepad(notepad_process)
                notepad_process = None
            elif "current time" in command or "time" in command:
                get_current_time()
            else:
                speak("I am not sure how to help with that.")

if __name__ == "__main__":
    main()

