# import necessary packages
import subprocess

class Apps():
    def __init__(self):
        pass

    def openApps(self, app_name):
        self.app_name = app_name
        installed_apps_root_path = r'C:\Program Files\Notepad++\notepad++.exe'
        subprocess.Popen(installed_apps_root_path)

# # Testing
# bot = Apps()
# bot.openApps('note')
