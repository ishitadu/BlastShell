# Copyright (c) 2020 Anindya Shiddhartha, licensed under MIT License.
# Read the LICENSE and README.md file for more information.
# You are only allowed to make changes to the code if you have the license file of the project.

print("This will take a few moments...")

# Program variables.
Version = "1.3Pre3"
Patch_Date = "13.07.2020 July"
License = "(c) 2020 Anindya Shiddhartha. All rights reserved."

# Mathematical variables.
math_mem =0
math_contval =0

# Modules to use!
import time

import os
dir_path = os.getcwd()

import socket

import random

import youtube_dl

from win32com.client import Dispatch
S = Dispatch("SAPI.SpVoice")

from datetime import datetime

from fractions import Fraction

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
    print("\u001b[0m")
    user_command = input(dir_path + ">\u001b[36m ")
    print("\u001b[0m")

    if (user_command == "about" or user_command == "ABOUT"):
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
        print("\u001b[0m")

    elif (user_command == "help" or user_command == "HELP"):
        print()
        print("CLS        Refreshes the screen.")
        print("CLOCK      Displays current date and time.")
        print("CRDIR      Creates a directory in current working directory.")
        print("CTEXT      Executes text file builder which enables user to create & modify")
        print("           text files.")
        print("DEL        Removes a file or directory.")
        print("DEVICE     Displays device specifications in detail.")
        print("EXIT       Terminates the shell.")
        print("IPCONF     Displays device's hostname and IP address.")
        print("MATH       Executes mathematical console.")
        print("RESTART    Restarts device.")
        print("SPEAK      Speaks a text given by user.")
        print("SETCD      Sets current working directory to a given path.")
        print("SHUTDOWN   Turns off device.")
        print("VDL        Downloads a specific video from YouTube as well as from")
        print("           other destinations when executed. (as video/audio)")
        print("WEBENT     Enables console to enter specific or custom")
        print("           websites.")
        print()

    elif (user_command == "exit" or user_command == "EXIT"):
        print("Closing shell...")
        break 

    elif (user_command == "shutdown" or user_command == "SHUTDOWN"):
        shutdown_confirm = input("Confirm device shutdown? (yes/no): ")

        if (shutdown_confirm == "yes" or shutdown_confirm == "YES"):
            print(), print("\u001b[32mShutting down...\u001b[0m")
            os.system("shutdown /s /t 1")

        elif (shutdown_confirm == "no" or shutdown_confirm == "NO"):
            print(), print("\u001b[32mShutdown aborted!\u001b[0m")

        else:
            print(), print("\u001b[31mCommand not found! Try typing 'yes' or 'no'.\u001b[0m")

    elif (user_command == "restart" or user_command == "RESTART"):
        restart_confirm = input("Confirm device restart? (yes/no): ")

        if (restart_confirm == "yes" or restart_confirm == "YES"):
            print(), print("\u001b[32mRestarting...\u001b[0m")
            os.system("shutdown /r /t 1")

        elif (restart_confirm == "no" or restart_confirm == "NO"):
            print(), print("\u001b[32mRestart aborted!\u001b[0m")

        else:
            print(), print("\u001b[31mCommand not found! Try typing 'yes' or 'no'.")


    elif (user_command == "setcd" or user_command == "SETCD"):
        dir_path = input("Path: ")

        try:
            os.chdir(dir_path)

        except:
            print(), print("\u001b[31mPath not found!\u001b[0m")
            dir_path = os.getcwd()

        else:
            print(), print("\u001b[32mPath set as current working directory.\u001b[0m")

    elif (user_command == "ipconf" or user_command == "IPCONF"):

        try: 
            host_name = socket.gethostname() 
            host_ip = socket.gethostbyname(host_name) 

        except: 
            print("\u001b[31mUnable to get hostname and IP address! Try again later.\u001b[0m")

        else:
            print()
            print("Hostname   : \u001b[32m" + host_name + "\u001b[0m") 
            print("IP Address : \u001b[32m" + host_ip + "\u001b[0m") 
            print()

    elif (user_command == "ctext" or user_command == "CTEXT"):
        print("Executed text file builder. Type 'help' to show executable commands.")

        while True:
            print()
            ctext_command = input("Text Builder> ")
            print()

            if (ctext_command == "help" or ctext_command == "HELP"):
                print()
                print("CRT    Creates a text file in program directory.")
                print("CLS    Refreshes the screen.")
                print("EXIT   Terminates text file builder.")
                print("MOD    Created a text file with text in program") 
                print("       directory.")
                print()

            elif (ctext_command == "crt" or ctext_command == "CRT"):
                my_file = open("New Text Document.txt","w+")
                print("\u001b[32mFile created!\u001b[0m")
                break

            elif (ctext_command == "cls" or ctext_command == "CLS"):
                os.system('cls')

            elif (ctext_command == "mod" or ctext_command == "MOD"):
                my_file = open("New Text Document.txt","w+")
                my_file.write(input("Text: "))
                my_file = open("New Text Document.txt","w+")
                print(), print("\u001b[32mFile with text created successfully!\u001b[0m")
                break

            elif (ctext_command == "exit" or ctext_command == "EXIT"):
                break

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")

    elif (user_command == "math" or user_command == "MATH"):
        def add(x, y):
            return x + y

        def sub(x, y):
            return x - y

        def div(x, y):
            return x / y

        def multi(x, y):
            return x * y

        def sq(x):
            return x ** 2

        def xq(x, y):
            return x ** y

        def cube(x):
            return x ** 3

        print("Mathematical console enabled. Type 'help' to show executable commands.")

        while True:
            print()
            math_command = input("Math> ")
            print()

            if (math_command == "help" or math_command == "HELP"):
                print()
                print("ADD        Adds two numbers.")
                print("CLS        Refreshes the screen.")
                print("CNUMFRAQ   Converts a decimal number to a fraction.")
                print("CUBE       Cubes a number.")
                print("DIV        Divides one number with another.")
                print("EXIT       Quits mathematical console.")
                print("MEM        Shows values stored in math memory.")
                print("MULTI      Multiplies one number with another.")
                print("PI         Adds the value of pi to memory.")
                print("MEMCLS     Clears application maemory.")
                print("SQ         Squares a given value.")
                print("SUB        Subtracts one number with another.")
                print("XQ         Modify a number with a to-the-power value.")
                print()

            elif (math_command == "exit" or math_command == "EXIT"):
                break

            elif (math_command == "pi" or math_command == "PI"):
                pi_value = 3.1415926535897932384626433832

                if math_contval == 0:
                    math_mem += pi_value
                    math_contval += 1
                    print("Pi = \u001b[32m" + str(pi_value) + "\u001b[0m (Added to memory)")

                else:
                    print("Using previous memory results for main value."), print()
                    pi_action = input("Action (add/sub/div/multi): ")

                    if (pi_action == "add" or pi_action == "ADD"):
                        math_mem += pi_value
                        print(), print("Pi = \u001b[32m" + str(pi_value) + "\u001b[0m (Refreshed memory)")

                    elif (pi_action == "sub" or pi_action == "SUB"):
                        math_mem -= pi_value
                        print(), print("Pi = \u001b[32m" + str(pi_value) + "\u001b[0m (Refreshed memory)")

                    elif (pi_action == "div" or pi_action == "DIV"):
                        math_mem /= pi_value
                        print(), print("Pi = \u001b[32m" + str(pi_value) + "\u001b[0m (Refreshed memory)")

                    elif (pi_action == "multi" or pi_action == "MULTI"):
                        math_mem *= pi_value
                        print(), print("Pi = \u001b[32m" + str(pi_value) + "\u001b[0m (Refreshed memory)")

                    else:
                        print(), print("\u001b[31mAction not found! Try something else.\u001b[0m")

            elif (math_command == "cnumfraq" or math_command == "CNUMFRAQ"):

                try:
                    convfraq_num = float(input("Value <> "))

                except OverflowError:
                    print(), print("\u001b[31mResult too large to operate with!\u001b[0m")

                except ValueError:
                    print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                else:
                    print(), print("Fraction = \u001b[32m" + str(Fraction(convfraq_num)) + "\u001b[0m")

            elif (math_command == "xq" or math_command == "XQ"):
                
                if math_contval == 0:
                    xq_num1 = float(input("Primary Value <> "))
                    xq_num2 = float(input("To-The-Power Value <> "))

                    try:
                        sum = xq(xq_num1, xq_num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        print()
                        xq_num2 = float(input("To-The-Power Value <> "))
                        sum = xq(math_mem, xq_num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "cube" or math_command == "CUBE"):
                
                if math_contval == 0:

                    try:
                        cube_input = float(input("Value <> "))
                        sum = cube(cube_input)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        sum = cube(math_mem)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "sq" or math_command == "SQ"):
                
                if math_contval == 0:

                    try:
                        sq_input = float(input("Value <> "))
                        sum = sq(sq_input)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        sum = sq(math_mem)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "mem" or math_command == "MEM"):
                
                if math_mem == 0:
                    print("Mathematical memory is empty!")

                else:
                    print("Stored value: \u001b[32m" + str(math_mem) + "\u001b[0m")

            elif (math_command == "memcls" or math_command == "MEMCLS"):
                math_mem -= math_mem
                math_contval -= math_contval
                print("\u001b[32mCleared math memory!\u001b[0m")

            elif (math_command == "cls" or math_command == "CLS"):
                os.system('cls')

            elif (math_command == "add" or math_command == "ADD"):

                if math_contval == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = add(num1, num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        print()
                        num1 = float(input("Value <> "))
                        sum = add(math_mem, num1)
                        

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    else:
                        math_mem += num1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "sub" or math_command == "SUB"):

                if math_contval == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = sub(num1, num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        print()
                        num1 = float(input("Value <> "))
                        sum = sub(math_mem, num1)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    else:
                        math_mem -= num1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "div" or math_command == "DIV"):

                if math_contval == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = div(num1, num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        print()
                        num1 = float(input("Value <> "))
                        sum = div(math_mem, num1)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    else:
                        math_mem /= num1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "multi" or math_command == "MULTI"):

                if math_contval == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = multi(num1, num2)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print(), print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        math_contval += 1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value."), print()
                        num1 = float(input("Value <> "))
                        sum = multi(math_mem, num1)

                    except OverflowError:
                        print(), print("\u001b[31mResult too large to solve!\u001b[0m")

                    else:
                        math_mem *= num1
                        print(), print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")

    elif (user_command == "speak" or user_command == "SPEAK"):
        speechtext = input("Text to speak: ")
        S.Speak(speechtext)

    elif (user_command == "clock" or user_command == "CLOCK"):
        now = datetime.now()
        date_time = now.strftime("Date: " + "%d/%m/%Y" + " | Time: " + "%H:%M:%S")
        print(date_time)

    elif (user_command == "webent" or user_command == "WEBENT"):
        print("Executed web console! Type 'help' to show executable commands.")

        while True:
            print()
            webcommand = input("Web> ")
            print()

            if (webcommand == "help" or webcommand == "HELP"):
                print()
                print("CLS      Refreshes the screen.")
                print("CSITE    Opens a custom webpage given by user.")
                print("EXIT     Closes web console.")
                print("SITES    Shows a list of popular sites to open.")
                print()

            elif (webcommand == "csite" or webcommand == "CSITE"):
                website = input("Website link / URL: ")
                webbrowser.open(website, new=2)
                print("\u001b[32mWeb page opened successfully!\u001b[0m")
                break

            elif (webcommand == "exit" or webcommand == "EXIT"):
                break

            elif (webcommand == "cls" or webcommand == "CLS"):
                os.system('cls')

            elif (webcommand == "sites" or webcommand == "SITES"):

                while True:
                    print()
                    print("Enter site number in-line to open.")
                    print()
                    print("1  YouTube")
                    print("2  Facebook")
                    print("3  Wikipedia")
                    print("4  Google")
                    print("5  LinkedIn")
                    print("6  GitHub")
                    print()

                    sites_execute = input("Web/Sites> ")

                    if sites_execute == "1":
                        webbrowser.open('www.youtube.com', new=2)
                        print("\u001b[32mWeb page opened successfully! Returned to web console.\u001b[0m")
                        break

                    elif sites_execute == "2":
                        webbrowser.open('www.facebook.com', new=2)
                        print("\u001b[32mWeb page opened successfully! Returned to web console.\u001b[0m")
                        break

                    elif sites_execute == "3":
                        webbrowser.open('www.wikipedia.org', new=2)
                        print("\u001b[32mWeb page opened successfully! Returned to web console.\u001b[0m")
                        break

                    elif sites_execute == "4":
                        webbrowser.open('www.google.com', new=2)
                        print("\u001b[32mWeb page opened successfully! Returned to web console.\u001b[0m")
                        break

                    elif sites_execute == "5":
                        webbrowser.open('www.linkedin.com', new=2)
                        print("\u001b[32mWeb page opened successfully! Returned to web console.\u001b[0m")
                        break

                    elif sites_execute == "6":
                        webbrowser.open('www.github.com', new=2)
                        print("\u001b[32mWeb page opened successfully! Returned to web console.\u001b[0m")
                        break

                    else:
                        print("\u001b[31mWebsite didn't found in list, try again!\u001b[0m")

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")

    elif (user_command == "cls" or user_command == "CLS"):
        os.system('cls')

    elif (user_command == "crdir" or user_command == "CRDIR"):
        dir_name = input("Directory name: ")
        print()
        os.mkdir(dir_name)
        print("\u001b[32mDirectory created successfully!\u001b[0m")

    elif (user_command == "del" or user_command == "DEL"):

        while True:
            filetype = input("File type ('help' for commands): ")
            print()

            if (filetype == "help" or filetype == "HELP"):
                print()
                print("CLS    Refreshes the screen.")
                print("DIR    Assigns file type as directory.")
                print("DOC    Assigns file type as document.")
                print("EXIT   Returns to home.")
                print()
                print()

            elif (filetype == "cls" or filetype == "CLS"):
                os.system('cls')

            elif (filetype == "dir" or filetype == "DIR"):
                mydir = input("Directory path: ")
                print()

                try:
                    shutil.rmtree(mydir)
                    print("\u001b[32mDeleted directory successfully!\u001b[0m")
                    break

                except OSError:
                    print("\u001b[31mDirectory not found, try again.\u001b[0m"), print()

            elif (filetype == "doc" or filetype == "DOC"):
                mydoc = input("File path: ")
                print()

                if os.path.isfile(mydoc):
                    os.remove(mydoc)
                    print("\u001b[32mDeleted file successfully!\u001b[0m")
                    break

                else:
                    print("\u001b[31mFile not found, try again.\u001b[0m"), print()

            elif (filetype == "exit" or filetype == "EXIT"):
                break

            else:
                print("\u001b[31mFile type / command not recognized! Type 'help' to show executable commands.\u001b[0m")

    elif (user_command == "device" or user_command == "DEVICE"):
        print()
        print("Device platform  : \u001b[32m" + device_platform + "\u001b[0m")
        print("Chipset          : \u001b[32m" + processor + "\u001b[0m")
        print("Operating system : \u001b[32m" + operating_system + "\u001b[0m")
        print("Build            : \u001b[32m" + build + "\u001b[0m")
        print()

    elif (user_command == "vdl" or user_command == "VDL"):

        while True:
            def dwl_vid():
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([vidmain])

            vidformat = input("Download as (audio/video/exit): ")

            if (vidformat == "video" or vidformat == "VIDEO"):

                try:
                    ydl_opts = {}
                    print()
                    vidlink = input("Video link / URL: ")
                    print()
                    vidmain = vidlink.strip()
                    dwl_vid()

                except:
                    print(), print("\u001b[31mInvalid link! Try again with a valid video link / URL.\u001b[0m"), print()

                else:
                    print(), print("\u001b[32mVideo downloaded successfully!\u001b[0m")
                    break

            elif (vidformat == "audio" or vidformat == "AUDIO"):

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
                    print(), print("\u001b[31mInvalid link! Try again with a valid video link / URL.\u001b[0m"), print()

                else:
                    print(), print("\u001b[32mVideo successfully downloaded as audio.\u001b[0m")
                    break

            elif (vidformat == "exit" or vidformat == "EXIT"):
                break

            else:
                print(), print("\u001b[31mFormat not recognised! Type either video or audio for format selection.\u001b[0m"), print()

    else:
        print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")