# Copyright (c) 2020 Anindya Shiddhartha, licensed under MIT License.
# Read the LICENSE and README.md file for more information.
# You are only allowed to make changes to the code if you have the license file of the project.

# Program variables.
Version = "1.2"
Patch_Date = "02.07.2020 July, Python 3.8.3"
License = "(c) 2020 Anindya Shiddhartha. All rights reserved."

# Mathematical variables.
math_mem =0
math_contval =0

# Modules to use!
import time

import socket

import os
dir_path = os.getcwd()

def cls():
    os.system('cls')

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


print("BlastShell | Type 'help' or 'about' for more information.")
print(License)
print()

while True:
    print()
    user_command = input(dir_path + "> ")
    print()

    if user_command == "about":
        print()
        print("BlastShell | Version: " + Version)
        print("Last updated on " + Patch_Date)
        print()
        print()
        print("BlastShell is an interactive command line / shell developed by an")
        print("independent developer named HitBlast. It will help you to run many")
        print("useful commands! It is an open-source project, which means anyone")
        print("can contribute in it!")
        print()
        print("The shell will get updates regularly within it's lifetime.")
        print()
        print("If you are having any issues with the app or just want to give a")
        print("suggestion, feel free to share!")
        print()
        print()

    elif user_command == "help":
        print()
        print("math   - Executes mathematical console.")
        print("exit   - Terminates the shell.")
        print("speak  - Speaks a text / word / letter for user.")
        print("clock  - Displays current date and time.")
        print("web    - Executes web console.")
        print("cls    - Refreshes command window.")
        print("cdset  - Sets current working directory to a given path.")
        print("del    - Removes a file from a directory.")
        print("device - Displays computer specifications in detail.")
        print("ytdl   - Downloads a specific video from YouTube when executed.")
        print("         (as video / audio)")
        print("ctext  - Executes text file builder which enables user to create & modify")
        print("         text files.")
        print("ipconf - Displays device's hostname and IP address.")
        print()

    elif user_command == "exit":
        print("Closing shell...")
        break

    elif user_command == "cdset":
        dir_path = input("Path: ")

        try:
            os.chdir(dir_path)

        except:
            print()
            print("Path not found!")
            dir_path = os.getcwd()

    elif user_command == "ipconf":
        def get_Host_name_IP(): 

            try: 
                host_name = socket.gethostname() 
                host_ip = socket.gethostbyname(host_name) 
                print()
                print("Hostname   : ",host_name) 
                print("IP Address : ",host_ip) 
                print()

            except: 
                print("Unable to get hostname and IP address! Try again later.") 

        get_Host_name_IP()

    elif user_command == "ctext":
        print("Executed text file builder. Type 'help' to show executable commands.")

        while True:
            print()
            ctext_command = input("Text Builder> ")
            print()

            if ctext_command == "help":
                print()
                print("add  - Creates a text file in program directory.")
                print("mod  - Created a text file with text in program") 
                print("       directory.")
                print("exit - Terminates text file builder.")
                print("cls  - Refreshes command window.")
                print()

            elif ctext_command == "add":
                my_file = open("New Text Document.txt","w+")
                print("File created! Returned to home.")
                break

            elif ctext_command == "cls":
                cls()

            elif ctext_command == "mod":
                my_file = open("New Text Document.txt","w+")
                my_file.write(input("Text: "))
                my_file = open("New Text Document.txt","w+")
                print()
                print("File with text created successfully! Returned to home.")
                break

            else:
                print("Whoa! Command not found. Type 'help' to show executable commands.")

    elif user_command == "math":
        def add(x, y):
            return x + y

        def sub(x, y):
            return x - y

        def div(x, y):
            return x / y

        def multi(x, y):
            return x * y

        print("Mathematical console enabled. Type 'help' to show executable commands.")

        while True:
            print()
            math_command = input("Math> ")
            print()

            if math_command == "help":
                print()
                print("add    - Adds two numbers.")
                print("sub    - Subtracts one number with another.")
                print("div    - Divides one number with another.")
                print("multi  - Multiplies one number with another.")
                print("mem    - Shows values stored in math memory.")
                print("memcls - Clears application maemory.")
                print("cls    - Refreshes command window.")
                print("exit   - Quits mathematical console.")
                print()

            elif math_command == "exit":
                print("Successfully terminated mathematical console!")
                break

            elif math_command == "mem":
                
                if math_mem == 0:
                    print("Mathematical memory is empty!")

                else:
                    print("Stored value: " + str(math_mem))

            elif math_command == "memcls":
                math_mem -= math_mem
                math_contval -= math_contval
                print("Cleared math memory.")

            elif math_command == "cls":
                cls()

            elif math_command == "add":

                if math_contval == 0:
                    num1 = float(input("Value 1 <> "))
                    num2 = float(input("Value 2 <> "))
                    sum = add(num1, num2)
                    math_mem += sum
                    math_contval += 1
                    print(), print("Result: " + str(sum) + " (Added to memory)")

                else:
                    print("Using previous memory result for main value.")
                    print()
                    num1 = float(input("Value <> "))
                    sum = add(math_mem, num1)
                    math_mem += num1
                    print(), print("Result: " + str(sum) + " (Refreshed memory)")

            elif math_command == "sub":

                if math_contval == 0:
                    num1 = float(input("Value 1 <> "))
                    num2 = float(input("Value 2 <> "))
                    sum = sub(num1, num2)
                    math_mem += sum
                    math_contval += 1
                    print(), print("Result: " + str(sum) + " (Added to memory)")

                else:
                    print("Using previous memory result for main value.")
                    print()
                    num1 = float(input("Value <> "))
                    sum = sub(math_mem, num1)
                    math_mem -= num1
                    print(), print("Result: " + str(sum) + " (Refreshed memory)")

            elif math_command == "div":

                if math_contval == 0:
                    num1 = float(input("Value 1 <> "))
                    num2 = float(input("Value 2 <> "))
                    sum = div(num1, num2)
                    math_mem += sum
                    math_contval += 1
                    print(), print("Result: " + str(sum) + " (Added to memory)")

                else:
                    print("Using previous memory result for main value.")
                    print()
                    num1 = float(input("Value <> "))
                    sum = div(math_mem, num1)
                    math_mem /= num1
                    print(), print("Result: " + str(sum) + " (Refreshed memory)")

            elif math_command == "multi":

                if math_contval == 0:
                    num1 = float(input("Value 1 <> "))
                    num2 = float(input("Value 2 <> "))
                    sum = multi(num1, num2)
                    math_mem += sum
                    math_contval += 1
                    print(), print("Result: " + str(sum) + " (Refreshed memory)")

                else:
                    print("Using previous memory result for main value.")
                    print()
                    num1 = float(input("Value <> "))
                    sum = multi(math_mem, num1)
                    math_mem *= num1
                    print(), print("Result: " + str(sum) + " (Refreshed memory)")

            else:
                print("Whoa! Command not found! Try typing 'help' to show executable commands.")

    elif user_command == "speak":
        text_to_speech = input("Text to speak: ")
        S.Speak(text_to_speech)

    elif user_command == "clock":
        now = datetime.now()
        dt_string = now.strftime("Date: " + "%d/%m/%Y" + " | Time: " + "%H:%M:%S")
        print(dt_string)

    elif user_command == "web":
        print("Executed web console! Type 'help' to show executable commands.")

        while True:
            print()
            webcommand = input("Web> ")
            print()

            if webcommand == "help":
                print()
                print("csite - Opens a custom webpage given by user.")
                print("sites - Shows a list of popular sites to open.")
                print("cls   - Refreshes command window.")
                print("exit  - Closes web console.")
                print()

            elif webcommand == "csite":
                website = input("Website link / URL: ")
                webbrowser.open(website, new=2)
                print("Web page opened successfully! Returned to home.")
                break

            elif webcommand == "exit":
                print("Successfully terminated web console!")
                break

            elif webcommand == "cls":
                cls()

            elif webcommand == "sites":
                while True:
                    print()
                    print("Enter site number in-line to open.")
                    print()
                    print("1. YouTube")
                    print("2. Facebook")
                    print("3. Wikipedia")
                    print("4. Google")
                    print("5. LinkedIn")
                    print("6. GitHub")
                    print()

                    sites_execute = input("Web/Sites> ")

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

                    elif sites_execute == "6":
                        webbrowser.open('www.github.com', new=2)
                        print("Web page opened successfully! Returned to web console.")
                        break

                    else:
                        print("Website didn't found in list, try again!")

            else:
                print("Whoa! Command not found. Try typing 'help' to show executable commands.")

    elif user_command == "cls":
        cls()

    elif user_command == "del":
        while True:
            filetype = input("File type ('help' for commands): ")
            print()

            if filetype == "help":
                print()
                print("dir  - Assigns file as directory.")
                print("doc  - Assigns file as document.")
                print("cls  - Refreshes command window.")
                print("exit - Returns to home.")
                print()

            elif filetype == "cls":
                cls()

            elif filetype == "dir":
                mydir = input("Directory path: ")
                print()

                try:
                    shutil.rmtree(mydir)
                    print("Deleted directory successfully! Returned to home.")
                    break

                except OSError as e:
                    print("Directory not found, try again.")
                    print()

            elif filetype == "doc":
                mydoc = input("File path: ")
                print()

                if os.path.isfile(mydoc):
                    os.remove(mydoc)
                    print("Deleted file successfully! Returned to home.")
                    break

                else:
                    print("File not found, try again.")
                    print()

            elif filetype == "exit":
                print("Successfully returned to home.")
                break

            else:
                print("File type / command not recognized! Type 'help' to show executable commands.")

    elif user_command == "device":
        print()
        print("Device platform  : " + device_platform)
        print("Chipset          : " + processor)
        print("Operating system : " + operating_system)
        print("Build            : " + build)
        print()

    elif user_command == "ytdl":

        while True:
            def dwl_vid():
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([vidmain])


            vidformat = input("Download as (audio/video): ")
            print()

            if vidformat == "video":
                ydl_opts = {}
                link_of_the_video = input("Video link / URL: ")
                print()
                vidmain = link_of_the_video.strip()
                dwl_vid()
                print()
                print("Done! Returned to home.")

            elif vidformat == "audio":
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }

                print()
                link_of_the_video = input("Video link / URL: ")
                print()
                vidmain = link_of_the_video.strip()
                dwl_vid()
                print()
                print("Done! Returned to home.")

            else:
                print("Format not recognised! Type either video or audio for format selection.")

    else:
        print("Whoa! Command not found. Try typing 'help' to show executable commands.")