"""
    Name: Saeed Mahmadzuber Ghasura
    Project: Voice Assistant
"""

# Import all the required libraries.

import tkinter as tk    # for creating GUI
import threading    # to handle speaking and listening simultaneously
import speech_recognition as sr    # to convert speech into text
import pyttsx3    # to convert text to speech
import requests    # to make HTTP requests to access web APIs
from datetime import datetime    # to fetch date and time
import sys    # to handle system specific parameters
import os    # to interact with OS

# This helps to locate resource files(in our case icons).
# '_MEIPASS' is a special attribute set by PyInstaller when it bundles a program into .exe 

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS    # bundled mode
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Initialize Text-to-Speech Engine (in our case, we used pyttsx3 library).
# Set basic properties of speech such as speech rate and volume.

tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)
tts_engine.setProperty('volume', 0.9)

# This converts provided text into speech.

def speak(text):
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

# This function is used to listen the command and also handles the microphone.
# Speech recognition library is used to handle listening.

def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            return text.lower()
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError:
        return "Sorry, there was an error with the request."
    except Exception as e:
        print(f"Error in listen function: {e}")
        return "An error occurred."
    
# Here, we get the weather using API from the website "openweathermap" and output it in formatted manner.
# I have set city to Ahmedabad by default.(which you can change accordingly)
# Also one can use their own API key.    

def get_weather():
    try:
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
            return f"The temperature in {city_name} is {temperature} degrees Celsius with {weather_description}."
        else:
            return "City not found."
    except Exception as e:
        print(f"Error in get_weather function: {e}")
        return "An error occurred while fetching weather."

# Here, current date and time is fetched using datetime library and is formatted for output to the user.

def get_current_time():
    try:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    except Exception as e:
        print(f"Error in get_current_time function: {e}")
        return "An error occurred while fetching the time."

# This handles all commands supported by our voice assistant.
# We can add/remove commands and modify accordingly to handle them.

def handle_command(command):
    if "stop" in command or "goodbye" in command or "exit" in command:
        return "Goodbye!"
    elif "hi" in command or "hello" in command or "how are you" in command:
        return "Hello! I'm doing well, thank you."
    elif "get weather" in command or "what is the weather today" in command:
        return get_weather()
    elif "current time" in command or "time" in command:
        return get_current_time()
    else:
        return "I'm not sure how to help with that."

# This is used to handle command processing in seperate thread.
# It updates the chat window and speak the response.
# In last, we handle exiting the app if user commands it to.

def handle_command_thread(command):
    response = handle_command(command)
    
    chat_window.config(state='normal')
    chat_window.insert(tk.END, f"Assistant: {response}\n")
    chat_window.config(state='disabled')
    chat_window.yview(tk.END)
    
    threading.Thread(target=speak, args=(response,)).start()
    
    if response == "Goodbye!":
        root.after(100, root.destroy)  

# It handles the submission of user input.         

def on_submit(event=None):
    if input_mode == "speak":
        threading.Thread(target=handle_command_thread, args=(listen(),)).start()
    elif input_mode == "type":
        command = input_entry.get()
        input_entry.delete(0, tk.END)
        chat_window.config(state='normal')
        chat_window.insert(tk.END, f"You: {command}\n")
        chat_window.config(state='disabled')
        chat_window.yview(tk.END)
        threading.Thread(target=handle_command_thread, args=(command,)).start()

# It handles switching of input modes.

def toggle_input_mode():
    global input_mode
    if input_mode == "speak":
        input_mode = "type"
        mode_button.config(image=keyboard_icon)
        input_entry.config(state='normal')
    else:
        input_mode = "speak"
        mode_button.config(image=microphone_icon)
        input_entry.config(state='disabled')

# Creating the GUI using Tkinter.        

root = tk.Tk()
root.title("Voice Assistant")

root.state("zoomed")

input_mode = "speak"  

microphone_icon = tk.PhotoImage(file=resource_path("Icons/icons8-microphone-24.png"))
keyboard_icon = tk.PhotoImage(file=resource_path("Icons/icons8-keyboard-30.png"))

chat_window = tk.Text(root, bg="#34495e", fg="white", font=("Arial", 12), state='disabled', wrap='word')
chat_window.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

input_entry = tk.Entry(root, bg="#ecf0f1", font=("Arial", 14), state='disabled')
input_entry.pack(pady=10, padx=10, fill=tk.X)
input_entry.bind('<Return>', on_submit)  

mode_button = tk.Button(root, image=microphone_icon, bg="#1abc9c", command=toggle_input_mode)
mode_button.pack(pady=5)

submit_button = tk.Button(root, text="Submit", bg="#3498db", fg="white", font=("Arial", 14), command=on_submit)
submit_button.pack(pady=5)

root.mainloop()
