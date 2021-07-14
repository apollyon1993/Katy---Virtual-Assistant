import pyttsx3
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voices', voices[-2].id)

engine.say("Olá, eu sou a Katy, sua assistente virtual")
engine.runAndWait()