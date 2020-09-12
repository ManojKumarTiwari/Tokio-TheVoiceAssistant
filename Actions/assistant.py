# import the necessary packages
from Automation.Web import wikipedia, movie_review, play_song, recommendation, open_website
from Automation.OS.Windows import open_installed_apps, create_and_write_file
from Senses import listen, speak

import os
import platform
import subprocess

def assist(command):
    """if statements for executing commands"""
    if "information" in command:
        speak.tokioResponse("information about what?")
        topic = listen.myCommand()
        try:
            bot = wikipedia.info()
            bot.get_info(topic)
        except Exception as e:
            print(e)

    elif "review" in command:
        speak.tokioResponse("which movie?")
        movie_name = listen.myCommand()
        try:
            bot = movie_review.Movie()
            bot.movie_review(movie_name)
        except Exception as e:
            print(e)

    elif "play song" in command:
        speak.tokioResponse("which song?")
        song_name = listen.myCommand()
        try:
            bot = play_song.Music()
            bot.fromytvideo(song_name)
        except Exception as e:
            print(e)

    elif "recommend" in command:
        try:
            bot = recommendation.IMDBlatestBestMovies()
            bot.recommend()
        except Exception as e:
            print(e)

    elif "open website" in command:
        speak.tokioResponse("which website?")
        website_name = listen.myCommand()
        try:
            bot = open_website.Website()
            bot.open_website(website_name)
        except Exception as e:
            print(e)

    else:
        # Check for OS
        if platform.system().lower() == 'windows':
            if "open" in command:
                speak.tokioResponse("which app?")
                app_name = listen.myCommand()
                try:
                    bot = open_installed_apps.Apps()
                    bot.openApps(app_name)
                    speak.tokioResponse("opened " + app_name + "sir")
                except Exception as e:
                    print(e)

            elif "create new" in command:
                speak.tokioResponse("What should I make note of")
                list_of_commands = []
                while listen.myCommand() != 'stop please':
                    list_of_commands.append(listen.myCommand() + '\n')
                try:
                    bot = create_and_write_file.CreateNewFile()
                    bot.takenote(list_of_commands)
                    speak.tokioResponse("Note taken sir!!")
                except Exception as e:
                    print(e)





