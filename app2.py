import os
import speech_recognition as sr  # Converts voice commands to text 
import pyttsx3  # Reads out text output to voice
import webbrowser 
from transformers import pipeline  # Hugging Face Transformers library for free LLM

# Initialize the Hugging Face Transformers pipeline for text generation
model_name = "gpt2"  # You can use any free model from Hugging Face, like "gpt2"
generator = pipeline('text-generation', model=model_name)

# Function to generate a reply using Hugging Face models
def Reply(question):
    response = generator(question, max_length=100, num_return_sequences=1)
    answer = response[0]['generated_text']
    return answer

# Text to speech setup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, how are you?")

# Function to take voice input from the user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print('Listening .......')
        r.pause_threshold = 1  # Wait for 1 sec before considering the end of a phrase
        audio = r.listen(source)
    try: 
        print('Recognizing ....')
        query = r.recognize_google(audio, language='en-in')
        print("User Said: {} \n".format(query))
    except Exception as e:
        print("Say that again .....")
        return "None"
    return query

# Main loop
if __name__ == '__main__':
    while True: 
        query = takeCommand().lower()
        if query == 'none':
            continue
        
        # Generate a response using Hugging Face model
        ans = Reply(query)
        print(ans)
        speak(ans)
        
        # Specific Browser Related Tasks 
        if "open youtube" in query: 
            webbrowser.open('www.youtube.com')
        if "open google" in query: 
            webbrowser.open('www.google.com')
        if "bye" in query:
            break
