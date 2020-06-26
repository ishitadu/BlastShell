# Copyright (c) 2020 Anindya Shiddhartha
# Read the LICENSE and README.md file for more information.
# You are only allowed to make changes to the code if you have the license file of the project.

# Important system variables.

Version = "1.1"
Creator = "HitBlast"
Patch_Date = "26.06.2020 June, Python 3.8.3"
License = "(c) 2020 Anindya Shiddhartha. All rights reserved."


# Modules to use!

import time

import os
def cls():
    os.system("clear")


import youtube_dl

from win32com.client import Dispatch
S = Dispatch("SAPI.SpVoice")

from datetime import datetime

import webbrowser

import shutil

import platform
device_platform = platform.machine()
processor = platform.processor()
operating_system = platform.system()
build = platform.version()

# End module importing!


# Main interface is written below.

dir_path = os.path.dirname(os.path.realpath(__file__))

print("BlastShell | Type 'help' or 'about' for more info. ")
print(License)
print()

while True:
    print()
    user_command = input(dir_path + "> ")
    print()

    if user_command == "about":
        print("=========================================================================")
        print("BlastShell | Created By " + Creator + " | Version: " + Version)
        print("Last updated on " + Patch_Date)
        print("-------------------------------------------------------------------------")
        print()
        print("BlastShell is an interactive command line / shell developed by an independent")
        print("developer named HitBlast. It will help you to run many useful commands!")
        print("It is an open-source project, which means anyone can contribute in it!")
        print()
        print("The shell will get updates regularly within it's lifetime.")
        print()
        print("If you are having any issues with the app or just want to give a suggestion,")
        print("feel free to share!")
        print()
        print("=========================================================================")

    elif user_command == "help":
        print("=================================================================")
        print("                          COMMANDS MENU")
        print("-----------------------------------------------------------------")
        print("add    - Executes addition console.")
        print("sub    - Executes subtraction console.")
        print("div    - Executes divide console.")
        print("multi  - Executes multiplication console.")
        print("exit   - Terminates the shell.")
        print("speak  - Speaks a text / word / letter for user.")
        print("clock  - Displays current date and time.")
        print("webbie - Executes web console window.")
        print("cls    - Refreshes command window.")
        print("del    - Removes a file from a directory.")
        print("device - Displays computer specifications in detail.")
        print("ytdl   - Downloads a specific video from YouTube when executed.")
        print("         (as video / audio)")
        print("=================================================================")

    elif user_command == "exit":
        print("Closing shell...")
        time.sleep(1)
        break

    elif user_command == "add":
        def add(x, y):
            return x + y


        num1 = float(input("Value 1 <> "))
        num2 = float(input("Value 2 <> "))
        res = add(num1, num2)

        print()
        print("Result's below!")
        print("-----------------------------------")
        print(res)

    elif user_command == "sub":
        def sub(x, y):
            return x - y


        num1 = float(input("Value 1 <> "))
        num2 = float(input("Value 2 <> "))
        res = sub(num1, num2)

        print()
        print("Result's below!")
        print("-----------------------------------")
        print(res)

    elif user_command == "div":
        def div(x, y):
            return x / y


        num1 = float(input("Value 1 <> "))
        num2 = float(input("Value 2 <> "))
        res = div(num1, num2)

        print()
        print("Result's below!")
        print("-----------------------------------")
        print(res)

    elif user_command == "multi":
        def multiply(x, y):
            return x * y


        num1 = float(input("Value 1 <> "))
        num2 = float(input("Value 2 <> "))
        res = multiply(num1, num2)

        print()
        print("Result's below!")
        print("-----------------------------------")
        print(res)

    elif user_command == "speak":
        text_to_speech = input("Enter text to say: ")
        S.Speak(text_to_speech)

    elif user_command == "clock":
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y" + " - " + "%H:%M:%S")
        print("Current date and time: ", dt_string)

    elif user_command == "webbie":
        print("Executed web console! Type 'helpweb' for executable commands.")

        while True:
            print()
            webcommand = input("> ")
            print()

            if webcommand == "helpweb":
                print("csite - Opens a custom webpage given by user.")
                print("sites - Shows a list of popular sites to open.")
                print("exit  - Closes web console.")

            elif webcommand == "csite":
                website = input("Enter website to open: ")
                webbrowser.open(website, new=2)
                print("Web page opened successfully! Returned to home.")
                break

            elif webcommand == "exit":
                print("Successfully terminated web console!")
                break

            elif webcommand == "sites":
                while True:
                    print("Type the number of site in prompt to open! Or, type 'exit' to close window.")
                    print()
                    print("1. YouTube")
                    print("2. Facebook")
                    print("3. Wikipedia")
                    print("4. Google")
                    print("5. LinkedIn")
                    print()

                    sites_execute = input("> ")

                    if sites_execute == "1":
                        webbrowser.open('www.youtube.com', new=2)
                        print("Web page opened successfully! Returned to web console.")
                        break

                    elif sites_execute == "2":
                        webbrowser.open('www.facebook.com', new=2)
                        print("Web page opened successfully! Returned to web console.")
                        break

                    elif sites_execute == "3":
                        webbrowser.open('www.wikipedia.org', new=2)
                        print("Web page opened successfully! Returned to web console.")
                        break

                    elif sites_execute == "4":
                        webbrowser.open('www.google.com', new=2)
                        print("Web page opened successfully! Returned to web console.")
                        break

                    elif sites_execute == "5":
                        webbrowser.open('www.linkedin.com', new=2)
                        print("Web page opened successfully! Returned to web console.")
                        break

                    else:
                        print("Website didn't found in list, try again!")

            else:
                print("Whoa! Command not found. Try typing 'helpweb' for executable commands.")

    elif user_command == "cls":
        cls()
        print("BlastShell | Type 'help' or 'about' for more info. ")
        print(License)
        print()

    elif user_command == "del":
        while True:
            filetype = input("Enter file type ('helpdel' for commands): ")
            print()

            if filetype == "helpdel":
                print("dir  - Assigns file as directory.")
                print("doc  - Assigns file as document.")
                print("exit - Returns to home.")
                print()

            elif filetype == "dir":
                mydir = input("Enter directory path: ")
                print()

                try:
                    shutil.rmtree(mydir)
                    print("Deleted directory successfully! Returned to home.")
                    break

                except OSError as e:
                    print("Directory not found, try again.")
                    print()

            elif filetype == "doc":
                mydoc = input("Enter file path: ")
                print()

                if operating_system.path.isfile(mydoc):
                    operating_system.remove(mydoc)
                    print("Deleted file successfully! Returned to home.")
                    break

                else:
                    print("File not found, try again.")
                    print()

            elif filetype == "exit":
                print("Successfully returned to home.")
                break

            else:
                print("File type / command not recognized! Type 'helpdel' for executable commands.")

    elif user_command == "device":
        print("=======================================")
        print("             YOUR DEVICE")
        print("---------------------------------------")
        print("Device platform  : " + device_platform)
        print("Chipset          : " + processor)
        print("Operating system : " + operating_system)
        print("Build            : " + build)
        print("=======================================")

    elif user_command == "ytdl":

        def dwl_vid():
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([vidmain])


        vidformat = input("Download video as ('aud' for audio and 'vid' for video): ")
        print()

        if vidformat == "vid":
            ydl_opts = {}
            link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download: ")
            print()
            vidmain = link_of_the_video.strip()
            dwl_vid()
            print()
            print("Done! Returned to home.")

        elif vidformat == "aud":
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

            print()
            link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download: ")
            print()
            vidmain = link_of_the_video.strip()
            dwl_vid()
            print()
            print("Done! Returned to home.")

        else:
            print("Format not recognised! Returned to home.")

    else:
        print("Whoa! Command not found. Try typing 'help' for executable commands.")
