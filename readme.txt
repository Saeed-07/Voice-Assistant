# Voice Assistant

This project is a voice assistant that uses speech recognition and text-to-speech (TTS) capabilities to perform tasks like reporting the weather, opening and closing Notepad, and telling the current time.

## Features

- Speech recognition using Google Speech Recognition API
- Text-to-speech responses using pyttsx3
- Fetches current weather information for a specified city
- Opens and closes Notepad
- Tells the current time

## Requirements

- Python 3.7 or higher
- Internet connection for fetching weather data

## Installation

1. Download the `voice_assistant.py` file to your local machine.

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the necessary dependencies:
    ```bash
    pip install SpeechRecognition pyttsx3 requests pywin32 pypiwin32
    ```

## Configuration

1. Update the `api_key` in the `get_weather` function within `voice_assistant.py` with your OpenWeatherMap API key:
    ```python
    api_key = "your_openweathermap_api_key"
    ```

2. (Optional) Change the `city_name` in the `get_weather` function to your preferred city:
    ```python
    city_name = "YourCity"
    ```

## Usage

1. Run the `voice_assistant.py` script:
    ```bash
    python voice_assistant.py
    ```

2. Follow the prompts and give voice commands. Available commands include:
    - "hello"
    - "how are you"
    - "get weather" or "what is the weather today"
    - "open notepad"
    - "close notepad"
    - "current time" or "time"
    - "stop", "goodbye", or "exit"

## Troubleshooting

- Make sure your microphone is properly connected and recognized by your system.
- Ensure you have an active internet connection for weather data retrieval.
- If you encounter issues with the pyttsx3 library, refer to the [pyttsx3 documentation](https://pyttsx3.readthedocs.io/).


Thanks.
Saeed Ghasura.
