# import necessary packages
import subprocess
from datetime import datetime

class CreateNewFile():
    def __init__(self):
        pass

    def takenote(self, text):
        date = datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(str(text))

        subprocess.Popen(["notepad.exe", file_name])

# # Testing
# bot = CreateNewFile()
# bot.takenote("this is a test text")

