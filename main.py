# Copyright (c) 2020 Anindya Shiddhartha, licensed under MIT License.
# Read the LICENSE and README.md file for more information.
# You are only allowed to make changes to the code if you have the license file of the project.

# Program variables.
Version = "1.3Pre1"
Patch_Date = "10.07.2020 July"
License = "(c) 2020 Anindya Shiddhartha. All rights reserved."

# Mathematical variables.
math_mem =0
math_contval =0

# Modules to use!
print("This will take a few moments...")

import time

import os
dir_path = os.getcwd()

import socket

import random

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
os.system('cls')
print("BlastShell | Type 'help' or 'about' for more information.")
print(License)
print()

while True:
    print("\u001b[39m")
    user_command = input(dir_path + ">\u001b[36m ")
    print("\u001b[39m")

    if user_command == "about":
        print()
        print("\033[1;34mBlastShell\u001b[39m | Version: " + Version)
        print("Last updated on " + Patch_Date)
        print("Licensed under MIT; Copyright " + License)
        print()
        print("An open-source interactive command line interface / shell developed mainly")
        print("for solving complex mathematical problems and for accomplishing day-to-day")
        print("tasks. BlastShell has a handful of useful commands available inside it, so")
        print("that users can use this application freely, without having to use internet")
        print("connection.")
        print()
        print("BlastShell gets updated frequently in order to maintain stable experience,")
        print("and also to introduce new commands and features to the users of it.")
        print()
        print("Reach / Support: hitblastofficial@gmail.com")
        print()

    elif user_command == "help":
        print()
        print("cls       Refreshes the screen.")
        print("clock     Displays current date and time.")
        print("crdir     Creates a directory in current working directory.")
        print("ctext     Executes text file builder which enables user to create & modify")
        print("          text files.")
        print("del       Removes a file or directory.")
        print("device    Displays computer specifications in detail.")
        print("exit      Terminates the shell.")
        print("ipconf    Displays device's hostname and IP address.")
        print("math      Executes mathematical console.")
        print("speak     Speaks a text given by user.")
        print("setcd     Sets current working directory to a given path.")
        print("vdl       Downloads a specific video from YouTube as well as from")
        print("          other destinations when executed. (as video/audio)")
        print("webent    Enables console to enter specific or custom")
        print("          websites.")
        print()

    elif user_command == "exit":
         print("Closing shell...")
         break 

    elif user_command == "setcd":
        dir_path = input("Path: ")

        try:
            os.chdir(dir_path)

        except:
            print()
            print("\u001b[31mPath not found!\u001b[39m")
            dir_path = os.getcwd()

        else:
            print()
            print("Path set as current working directory.")

    elif user_command == "ipconf":

        try: 
            host_name = socket.gethostname() 
            host_ip = socket.gethostbyname(host_name) 

        except: 
            print("\u001b[31mUnable to get hostname and IP address! Try again later.\u001b[39m")

        else:
            print()
            print("Hostname   : \u001b[32m" + host_name + "\u001b[39m") 
            print("IP Address : \u001b[32m" + host_ip + "\u001b[39m") 
            print()

    elif user_command == "ctext":
        print("Executed text file builder. Type 'help' to show executable commands.")

        while True:
            print()
            ctext_command = input("Text Builder> ")
            print()

            if ctext_command == "help":
                print()
                print("add    Creates a text file in program directory.")
                print("cls    Refreshes the screen.")
                print("exit   Terminates text file builder.")
                print("mod    Created a text file with text in program") 
                print("       directory.")
                print()

            elif ctext_command == "add":
                my_file = open("New Text Document.txt","w+")
                print("File created!")
                break

            elif ctext_command == "cls":
                os.system('cls')

            elif ctext_command == "mod":
                my_file = open("New Text Document.txt","w+")
                my_file.write(input("Text: "))
                my_file = open("New Text Document.txt","w+")
                print()
                print("File with text created successfully!")
                break

            elif ctext_command == "exit":
                break

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[39m")

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
                print("add      Adds two numbers.")
                print("cls      Refreshes the screen.")
                print("cube     Cubes a number.")
                print("div      Divides one number with another.")
                print("exit     Quits mathematical console.")
                print("mem      Shows values stored in math memory.")
                print("multi    Multiplies one number with another.")
                print("memcls   Clears application maemory.")
                print("sq       Squares a given value.")
                print("sub      Subtracts one number with another.")
                print()

            elif math_command == "exit":
                break

            elif math_command == "cube":
                
                if math_contval == 0:

                    try:
                        cube = float(input("Value <> "))
                        sum = cube ** 3

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        sum = math_mem ** 3

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Refreshed memory)")

            elif math_command == "sq":
                
                if math_contval == 0:

                    try:
                        sq = float(input("Value <> "))
                        sum = sq ** 2

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        sum = math_mem ** 2

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Refreshed memory)")

            elif math_command == "mem":
                
                if math_mem == 0:
                    print("Mathematical memory is empty!")

                else:
                    print("Stored value: \u001b[32m" + str(math_mem) + "\u001b[39m")

            elif math_command == "memcls":
                math_mem -= math_mem
                math_contval -= math_contval
                print("Cleared math memory!")

            elif math_command == "cls":
                os.system('cls')

            elif math_command == "add":

                if math_contval == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = add(num1, num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        print()
                        num1 = float(input("Value <> "))
                        sum = add(math_mem, num1)
                        

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem += num1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Refreshed memory)")

            elif math_command == "sub":

                if math_contval == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = sub(num1, num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        print()
                        num1 = float(input("Value <> "))
                        sum = sub(math_mem, num1)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem -= num1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Refreshed memory)")

            elif math_command == "div":

                if math_contval == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = div(num1, num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        print()
                        num1 = float(input("Value <> "))
                        sum = div(math_mem, num1)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem /= num1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Refreshed memory)")

            elif math_command == "multi":

                if math_contval == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = multi(num1, num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        print()
                        num1 = float(input("Value <> "))
                        sum = multi(math_mem, num1)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[39m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[39m")

                    else:
                        math_mem *= num1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[39m (Refreshed memory)")

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[39m")

    elif user_command == "speak":
        speechtext = input("Text to speak: ")
        S.Speak(speechtext)

    elif user_command == "clock":
        now = datetime.now()
        date_time = now.strftime("Date: " + "%d/%m/%Y" + " | Time: " + "%H:%M:%S")
        print(date_time)

    elif user_command == "webent":
        print("Executed web console! Type 'help' to show executable commands.")

        while True:
            print()
            webcommand = input("Web> ")
            print()

            if webcommand == "help":
                print()
                print("cls      Refreshes the screen.")
                print("csite    Opens a custom webpage given by user.")
                print("exit     Closes web console.")
                print("sites    Shows a list of popular sites to open.")
                print()

            elif webcommand == "csite":
                website = input("Website link / URL: ")
                webbrowser.open(website, new=2)
                print("Web page opened successfully! ")
                break

            elif webcommand == "exit":
                break

            elif webcommand == "cls":
                os.system('cls')

            elif webcommand == "sites":
                while True:
                    print()
                    print("Enter site number in-line to open.")
                    print()
                    print("1 YouTube")
                    print("2 Facebook")
                    print("3 Wikipedia")
                    print("4 Google")
                    print("5 LinkedIn")
                    print("6 GitHub")
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
                        print("\u001b[31mWebsite didn't found in list, try again!\u001b[39m")

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[39m")

    elif user_command == "cls":
        os.system('cls')

    elif user_command == "crdir":
        dir_name = input("Directory name: ")
        print()
        os.mkdir(dir_name)
        print("Directory created successfully!")

    elif user_command == "del":
        while True:
            filetype = input("File type ('help' for commands): ")
            print()

            if filetype == "help":
                print()
                print("cls    Refreshes the screen.")
                print("dir    Assigns file type as directory.")
                print("doc    Assigns file type as document.")
                print("exit   Returns to home.")
                print()
                print()

            elif filetype == "cls":
                os.system('cls')

            elif filetype == "dir":
                mydir = input("Directory path: ")
                print()

                try:
                    shutil.rmtree(mydir)
                    print("Deleted directory successfully!")
                    break

                except OSError:
                    print("\u001b[31mDirectory not found, try again.\u001b[39m")
                    print()

            elif filetype == "doc":
                mydoc = input("File path: ")
                print()

                if os.path.isfile(mydoc):
                    os.remove(mydoc)
                    print("Deleted file successfully!")
                    break

                else:
                    print("\u001b[31mFile not found, try again.\u001b[39m")
                    print()

            elif filetype == "exit":
                break

            else:
                print("\u001b[31mFile type / command not recognized! Type 'help' to show executable commands.\u001b[39m")

    elif user_command == "device":
        print()
        print("Device platform  : \u001b[32m" + device_platform + "\u001b[39m")
        print("Chipset          : \u001b[32m" + processor + "\u001b[39m")
        print("Operating system : \u001b[32m" + operating_system + "\u001b[39m")
        print("Build            : \u001b[32m" + build + "\u001b[39m")
        print()

    elif user_command == "vdl":

        while True:
            def dwl_vid():
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([vidmain])

            vidformat = input("Download as (audio/video/exit): ")

            if vidformat == "video":

                try:
                    ydl_opts = {}
                    print()
                    vidlink = input("Video link / URL: ")
                    print()
                    vidmain = vidlink.strip()
                    dwl_vid()

                except:
                    print()
                    print("\u001b[31mInvalid link! Try again with a valid video link / URL.\u001b[39m")
                    print()

                else:
                    print()
                    print("Done! ")
                    break

            elif vidformat == "audio":

                try:
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }

                    print()
                    vidlink = input("Video link / URL: ")
                    print()
                    vidmain = vidlink.strip()
                    dwl_vid()
                
                except:
                    print()
                    print("\u001b[31mInvalid link! Try again with a valid video link / URL.\u001b[39m")
                    print()

                else:
                    print()
                    print("Done! ")
                    break

            elif vidformat == "exit":
                break

            else:
                print("\u001b[31mFormat not recognised! Type either video or audio for format selection.\u001b[39m")
                print()

    else:
        print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[39m")