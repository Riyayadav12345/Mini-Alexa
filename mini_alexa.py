import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except Exception:
        speak("Sorry, I didn't catch that. Please say again.")
        return ""

def run_alexa():
    speak("Hello! I am Mini Alexa. How can I help you?")
    while True:
        query = listen()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        elif "stop" in query or "exit" in query:
            speak("Goodbye!")
            break

        else:
            speak("I am not sure about that. Please try again.")

if __name__ == "__main__":
    run_alexa()