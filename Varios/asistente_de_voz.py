import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate",120)
engine.setProperty("voice", "spanish")

engine.say("Hola mi niña bella")
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("You can talk right now ! ")
    audio = r.listen(source)
    text = r.recognize_google(audio,language="es-EC")
    print(text)
