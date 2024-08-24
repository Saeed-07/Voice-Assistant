```markdown
# Voice Assistant Project

## Project Overview

This is a Python-based Voice Assistant project that can recognize voice commands, convert text to speech, and perform tasks such as fetching the weather, telling the current time, and responding to greetings. The project is built with a graphical user interface (GUI) using the Tkinter library.

## Features

- **Speech Recognition**: Converts speech to text using the `speech_recognition` library.
- **Text-to-Speech**: Converts text to speech using the `pyttsx3` library.
- **Weather Fetching**: Retrieves weather data for a specified city using the OpenWeatherMap API.
- **Time Telling**: Provides the current time.
- **User Interaction**: Handles both typed and spoken commands.
- **GUI**: A user-friendly interface created using Tkinter.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**
- **pip** (Python package installer)

## Required Libraries

Install the required Python libraries by running the following command:

```bash
pip install tkinter threading speechrecognition pyttsx3 requests
```

Alternatively, you can install the dependencies listed in the `requirements.txt` file (if provided):

```bash
pip install -r requirements.txt
```

## Setup Instructions

1. **Clone the Repository**:

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/voice-assistant.git
   cd voice-assistant
   ```

2. **API Key for Weather Data**:

   The project uses the OpenWeatherMap API to fetch weather data. You need an API key to use this service.

   - Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API key.
   - Replace the `api_key` variable in the `get_weather()` function with your own API key:

   ```python
   api_key = "your_api_key_here"
   ```

3. **Run the Project**:

   Run the project using Python:

   ```bash
   python main.py
   ```

   This will launch the Voice Assistant's GUI.

## Usage

- **Switching Input Modes**: You can switch between voice and text input modes using the toggle button.
- **Submit a Command**: In voice mode, click the "Submit" button or press "Enter" to speak your command. In text mode, type your command in the input field and press "Enter".
- **Available Commands**:
  - "Hi", "Hello", "How are you" - The assistant will greet you.
  - "Get weather", "What is the weather today" - The assistant will provide the weather for Ahmedabad (default city).
  - "Current time", "Time" - The assistant will tell the current time.
  - "Stop", "Goodbye", "Exit" - The assistant will terminate the program.

## Packaging the Project (Optional)

To distribute the project as a standalone executable, you can use PyInstaller:

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Create the executable:

   ```bash
   pyinstaller --onefile --windowed main.py
   ```

   This will create a `dist` folder containing the executable file.

## Troubleshooting

- **Microphone Issues**: Ensure your microphone is properly configured and accessible by the program.
- **Weather Data Not Fetching**: Check your internet connection and ensure the API key is correctly set.
- **Dependencies Not Installed**: Double-check that all required libraries are installed.

## Contributing

Feel free to fork this repository, make your improvements, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

**Saeed Mahmadzuber Ghasura**

LinkedIn: [www.linkedin.com/in/saeedghasura](https://www.linkedin.com/in/saeedghasura)
```