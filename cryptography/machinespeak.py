import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate',250)
print(rate)
engine.say("Hello tarun Aggarwal i am your assistent created by you")
engine.runAndWait()