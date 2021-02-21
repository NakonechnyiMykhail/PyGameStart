import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume', 1.0)           # setting up volume level  between 0 and 1

name = str(input("What is your name? "))
engine.say("What is your name?") # .say(text)
engine.runAndWait()
if len(name) >= 3:
    engine.say(f"Hello, {name}")
    engine.runAndWait()