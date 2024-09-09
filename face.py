import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

assistant_name = "itachi"

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands
def listen():
    with sr.Microphone() as source:
        print(f"{assistant_name} is listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust microphone for ambient noise
        audio = recognizer.listen(source)

    try: 
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        return command.lower()

    except sr.UnknownValueError:
        print("yamate kudasai.")
        return ""

# Function to process commands
def process_command(command):
    if "hello" in command:
        speak(f"Hello! I'm {assistant_name}. How can I assist you?")

    elif "goodbye" in command:
        speak("Goodbye!")

    else:
        speak("yamate kudasai.")

# Main program loop
while True:
    command = listen()
    process_command(command)
#all the comments are for self explanations..