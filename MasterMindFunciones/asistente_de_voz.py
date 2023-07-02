import re
import pyttsx3
import speech_recognition as sr

# engine.say("Hola, ¿como estas?")
# engine.runAndWait()  # reproduce el audio


def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("voice", "spanish")
    engine.setProperty("rate", 120)
    return engine


def recognize_voice(r):
    with sr.Microphone() as source:
        print("Puedes hablar ahora...\n")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
        print(text, "\n")
    return text


def identify_name(text):
    patterns = ["me llamo ([A-Za-z]+)", "soy ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
            return name
        except IndexError:
            pass
            # print("No me ha dicho su nombre")
    return "Fallo"


def respuesta_de_nombre(name, engine):
    engine.say("Encantado de conocerte {}".format(name))
    engine.runAndWait()
    print("Encantado de conocerte {}\n".format(name))


def saludo(engine):
    engine.say("Hola, ¿como estas?")
    engine.say("¿Como te llamas?")
    engine.runAndWait()  # reproduce el audio


def main():
    r = sr.Recognizer()
    engine = initialize_engine()
    saludo(engine)
    text = recognize_voice(r)
    name = identify_name(text)
    if name != "Fallo":
        respuesta_de_nombre(name, engine)
    else:
        engine.say("no te entendi bien tu nombre, repitelo de nuevo")
        engine.runAndWait()
        print("\nno te he entendido bien, intentalo de nuevo...")


if __name__ == "__main__":
    main()
