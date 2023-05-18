import speech_recognition as sr
from google.cloud import language_v1

# Initialize the recognizer and Google Natural Language client
recognizer = sr.Recognizer()
client = language_v1.LanguageServiceClient()

# Set the AI assistant's name
assistant_name = "Itachi"

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
        print("Sorry, I didn't catch that.")
        return ""

# Function to analyze text using Google Natural Language API
def analyze_text(text):
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    response = client.analyze_sentiment(request={'document': document})

    sentiment_score = response.document_sentiment.score
    sentiment_magnitude = response.document_sentiment.magnitude

    return sentiment_score, sentiment_magnitude

# Function to process commands
def process_command(command):
    if "hello" in command:
        print(f"Hello! I'm {assistant_name}. How can I assist you?")

    elif "goodbye" in command:
        print("Goodbye!")

    else:
        sentiment_score, sentiment_magnitude = analyze_text(command)
        if sentiment_score >= 0.2:
            print("Positive sentiment detected.")
        elif sentiment_score <= -0.2:
            print("Negative sentiment detected.")
        else:
            print("Neutral sentiment detected.")

# Main program loop
while True:
    command = listen()
    process_command(command)
