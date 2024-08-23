import tkinter as tk
import threading
import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime
import sys
import os

def resource_path(relative_path):
    # Check if the application is bundled using PyInstaller
    if hasattr(sys, '_MEIPASS'):
        # If bundled, the path would be relative to _MEIPASS
        base_path = sys._MEIPASS
    else:
        # Otherwise, it's relative to the script
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)
tts_engine.setProperty('volume', 0.9)

def speak(text):
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print(f"Error in speak function: {e}")

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

def get_current_time():
    try:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."
    except Exception as e:
        print(f"Error in get_current_time function: {e}")
        return "An error occurred while fetching the time."

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

def handle_command_thread(command):
    response = handle_command(command)
    
    # Display the response before speaking
    chat_window.config(state='normal')
    chat_window.insert(tk.END, f"Assistant: {response}\n")
    chat_window.config(state='disabled')
    chat_window.yview(tk.END)
    
    threading.Thread(target=speak, args=(response,)).start()
    
    if response == "Goodbye!":
        root.after(100, root.destroy)  

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
