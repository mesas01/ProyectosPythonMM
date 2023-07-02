import pyttsx3
import speech_recognition as sr
from speech_recognition import UnknownValueError

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("voice", "spanish")

r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def hear_me():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-MX")
            print("He entendido: {}".format(text))
            return text
        except UnknownValueError:
            print("Lo siento pero no te he escuchado")
            return


if __name__ == "__main__":
    speak("probando la funcionalidad de todo")
    print(hear_me())
