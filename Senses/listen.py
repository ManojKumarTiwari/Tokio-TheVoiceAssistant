# import necessary packages
import speech_recognition as sr

def myCommand():
    """
    listens to commands spoken through microphone (audio)
    :returns text extracted from the speech which is our command
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1) # removed "duration=1" argument to reduce wait time
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand()
    except sr.RequestError as e:
        print("????")
    return command




