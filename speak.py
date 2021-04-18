import pyttsx3
def speak(text):

    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    print (rate)
    engine.setProperty('rate', 50)

    # voices = engine.getProperty('voices')
    # #engine.setProperty('voice', voices[0].id)  e
    # engine.setProperty('voice', voices[2].id)


    engine.say(text)
    engine.runAndWait()

