from Senses import listen, speak
from Actions import assistant

import os
import platform
import deepspeech
#
# open_installed_apps.open_installed_apps()
# print(os.name)
#
# print(platform.system()) # Operating System
# print(platform.release()) # Version of Operating System

# initial conversation
speak.tokioResponse("Hi Maddy, I am Tokio and I am your personal voice assistant. "
                    + "How may I help you?")

# "Please give a command or say 'help me' and I will tell you what all I can do for you."

#loop to continue executing multiple commands
while True:
    assistant.assist(listen.myCommand())
