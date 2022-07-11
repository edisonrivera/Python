import os
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate",120)
engine.setProperty("voice", "spanish")
engine.say("Habla ahora")
engine.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)
    text = r.recognize_google(audio,language="es-EC")
print(text)

os.startfile(r"C:\Program Files (x86)\EPSON\Epson Scan 2\Core\es2devedit.exe")