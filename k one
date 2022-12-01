import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('Voices')
engine.setProperty('voices',voices[0].id)
def talk():
    engine.say("I am your Assistant K one")
    engine.runAndWait()

def take_query():
    try:
        with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "kevin" in command:
            command = command.replace('kevin', '')
            print(command)
    else:
        print("Fails")
    return command

def run_kevin():
    command = take_query()
    print(command)
    if 'play' in command():
        song = command.replace('play','')
        talk("playing"+song)
        pk.playonyt(song)



while True:
    run_kevin()

# in wikipedia function replace empty string as well
# import pyjokes
