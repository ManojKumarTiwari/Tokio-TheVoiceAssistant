# import necessary packages
import pyttsx3 as p

def tokioResponse(audio):
    """speaks audio passed as argument"""
    engine = p.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    print(audio)
    for line in audio.splitlines():
        engine.say(audio)
    engine.runAndWait()