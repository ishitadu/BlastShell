# Copyright (c) 2020 Anindya Shiddhartha, licensed under MIT License.
# Read the LICENSE and README.md file for more information.

print("This will take a few moments...")

# Program variables.
Version = "1.32M"
Patch_Date = "20.07.2020 July"
License = "(c) 2020 Anindya Shiddhartha. All rights reserved."

# Mathematical memory variable.
math_mem =0

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
print(License + "\n")

while True:

    user_command = input("\u001b[0m\n" + dir_path + "> \u001b[36m")

    if (user_command == "about" or user_command == "ABOUT"):
        print("\n\n\033[1;34mBlastShell\u001b[0m | Version: " + Version)
        print("Last updated on " + Patch_Date)
        print("Licensed under MIT; Copyright " + License)
        print("\nAn easy-to-use interactive command line interface / shell developed mainly")
        print("for solving complex mathematical problems and for accomplishing day-to-day")
        print("tasks. BlastShell has a handful of useful commands available inside it, so")
        print("that users can use this application freely, without having to use internet")
        print("connection.")
        print("\nBlastShell gets updated frequently in order to maintain stable experience,")
        print("and also to introduce new commands and features to the users of it.")
        print("\nReach / Support: hitblastofficial@gmail.com\n")

    elif (user_command == "help" or user_command == "HELP"):
        print("\u001b[0m\n\nCLS        Refreshes the screen.")
        print("CLOCK      Displays current date and time.")
        print("CRDIR      Creates a directory in current working directory.")
        print("CTEXT      Executes text file builder which enables user to create & modify")
        print("           text files.")
        print("DEL        Removes a file or directory.")
        print("EXIT       Terminates the shell.")
        print("IPCONF     Displays device's hostname and IP address.")
        print("MATH       Executes mathematical console.")
        print("RESTART    Restarts device.")
        print("SYS        Displays device specifications in detail.")
        print("SPEAK      Speaks a text given by user.")
        print("SETCD      Sets current working directory to a given path.")
        print("SHUTDOWN   Turns off device.")
        print("VDL        Downloads a specific video from YouTube as well as from")
        print("           other destinations when executed. (as video/audio)")
        print("WEB        Enables console to enter specific or custom")
        print("           websites.\n")

    elif (user_command == "exit" or user_command == "EXIT"):
        print("\u001b[0mClosing shell...")
        break 

    elif (user_command == "shutdown" or user_command == "SHUTDOWN"):
        shutdown_confirm = input("\u001b[0mConfirm device shutdown? (yes/no): ")

        if (shutdown_confirm == "yes" or shutdown_confirm == "YES"):
            print("\u001b[32mShutting down...\u001b[0m")
            os.system("shutdown /s /t 1")

        elif (shutdown_confirm == "no" or shutdown_confirm == "NO"):
            print("\u001b[32mShutdown aborted!\u001b[0m")

        else:
            print("\u001b[31mCommand not found! Try typing 'yes' or 'no'.\u001b[0m")

    elif (user_command == "restart" or user_command == "RESTART"):
        restart_confirm = input("\u001b[0mConfirm device restart? (yes/no): ")

        if (restart_confirm == "yes" or restart_confirm == "YES"):
            print("\u001b[32mRestarting...\u001b[0m")
            os.system("shutdown /r /t 1")

        elif (restart_confirm == "no" or restart_confirm == "NO"):
            print("\u001b[32mRestart aborted!\u001b[0m")

        else:
            print("\u001b[31mCommand not found! Try typing 'yes' or 'no'.")

    elif (user_command == "setcd" or user_command == "SETCD"):
        dir_path = input("\u001b[0mPath: ")

        try:
            os.chdir(dir_path)

        except:
            print("\u001b[31mPath not found!\u001b[0m")
            dir_path = os.getcwd()

        else:
            print("\u001b[32mPath set as current working directory.\u001b[0m")

    elif (user_command == "ipconf" or user_command == "IPCONF"):

        try: 
            host_name = socket.gethostname() 
            host_ip = socket.gethostbyname(host_name) 

        except: 
            print("\u001b[31mUnable to get hostname and IP address! Try again later.\u001b[0m")

        else:
            print("\u001b[0m\n\nHostname   : \u001b[32m" + host_name + "\u001b[0m") 
            print("IP Address : \u001b[32m" + host_ip + "\u001b[0m\n") 

    elif (user_command == "ctext" or user_command == "CTEXT"):
        print("\u001b[0mExecuted text file builder. Type 'help' to show executable commands.")

        while True:
            ctext_command = input("\nText Builder> ")

            if (ctext_command == "help" or ctext_command == "HELP"):
                print("\n\nCRT    Creates a text file in program directory.")
                print("CLS    Refreshes the screen.")
                print("EXIT   Terminates text file builder.")
                print("MOD    Created a text file with text in program") 
                print("       directory.\n")

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
                print("\u001b[32mFile with text created successfully!\u001b[0m")
                break

            elif (ctext_command == "exit" or ctext_command == "EXIT"):
                break

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")

    elif (user_command == "math" or user_command == "MATH"):
        print("\u001b[0mMathematical console enabled. Type 'help' to show executable commands.")

        while True:
            math_command = input("\nMath> ")

            if (math_command == "help" or math_command == "HELP"):
                print("\n\nADD        Adds two numbers.")
                print("CLS        Refreshes the screen.")
                print("CUBE       Cubes a number.")
                print("DIV        Divides one number with another.")
                print("EXIT       Quits mathematical console.")
                print("MEM        Shows values stored in math memory.")
                print("MULTI      Multiplies one number with another.")
                print("NUMFRAQ    Converts a decimal number to a fraction.")
                print("PI         Adds the value of pi to memory.")
                print("PROFLOSS   Detects profit or loss by using purchase and selling value.")
                print("MEMCLS     Clears application maemory.")
                print("SQ         Squares a given value.")
                print("SUB        Subtracts one number with another.")
                print("XQ         Modify a number with a to-the-power value.\n")

            elif (math_command == "exit" or math_command == "EXIT"):
                break

            elif (math_command == "profloss" or math_command == "PROFLOSS"):

                try:
                    buy_value = float(input("Purchase Value <> "))
                    sell_value = float(input("Selling Value <> "))

                    if buy_value < sell_value:
                        sell_value -= buy_value
                        profloss_value = sell_value / buy_value * 100
                        output_type = ("Profit \u001b[32m")

                    elif buy_value > sell_value:
                        buy_value -= sell_value
                        profloss_value = buy_value / sell_value * 100
                        output_type = ("Loss \u001b[31m")

                    else:
                        buy_value -= sell_value
                        profloss_value = buy_value / sell_value * 100
                        output_type = ("None \u001b[32m")

                except ValueError:
                    print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                except OverflowError:
                    print("\u001b[31mResult too large to solve!\u001b[0m")

                else:
                    print("Result = " + output_type + "(" + str(profloss_value) + "%) \u001b[0m")

            elif (math_command == "pi" or math_command == "PI"):
                pi_value = 3.1415926535897932384626433832

                if math_mem == 0:
                    math_mem += pi_value
                    print("Pi = \u001b[32m" + str(pi_value) + "\u001b[0m (Added to memory)")

                else:
                    print("Using previous memory results for main value.")
                    pi_action = input("Action (add/sub/div/multi): ")

                    if (pi_action == "add" or pi_action == "ADD"):

                        try:
                            math_mem += pi_value

                        except OverflowError:
                            print("\u001b[31mMemory overload!\u001b[0m")

                        else:
                            print("Result = \u001b[32m" + str(math_mem) + "\u001b[0m (Refreshed memory)")

                    elif (pi_action == "sub" or pi_action == "SUB"):
                        
                        try:
                            math_mem -= pi_value

                        except OverflowError:
                            print("\u001b[31mMemory overload!\u001b[0m")

                        else:
                            print("Result = \u001b[32m" + str(math_mem) + "\u001b[0m (Refreshed memory)")

                    elif (pi_action == "div" or pi_action == "DIV"):
                        
                        try:
                            math_mem /= pi_value

                        except OverflowError:
                            print("\u001b[31mMemory overload!\u001b[0m")

                        else:
                            print("Result = \u001b[32m" + str(math_mem) + "\u001b[0m (Refreshed memory)")

                    elif (pi_action == "multi" or pi_action == "MULTI"):
                        
                        try:
                            math_mem *= pi_value

                        except OverflowError:
                            print("\u001b[31mMemory overload!\u001b[0m")

                        else:
                            print("Result = \u001b[32m" + str(math_mem) + "\u001b[0m (Refreshed memory)")

                    else:
                        print("\u001b[31mAction not found! Try something else.\u001b[0m")

            elif (math_command == "numfraq" or math_command == "NUMFRAQ"):

                if math_mem == 0:

                    try:
                        convfraq_num = float(input("Value <> "))

                    except OverflowError:
                        print("\u001b[31mResult too large to operate with!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        print("Fraction = \u001b[32m" + str(Fraction(convfraq_num)) + "\u001b[0m")

                else:
                    
                    try:
                        print("Using previous memory result for main value.")
                        convfraq_num = Fraction(math_mem)

                    except OverflowError:
                        print("\u001b[31mUnexpected value error occured!\u001b[0m")

                    else:
                        print("Fraction = \u001b[32m" + str(convfraq_num) + "\u001b[0m")

            elif (math_command == "xq" or math_command == "XQ"):

                def xq(x, y):
                    return x ** y
                
                if math_mem == 0:

                    try:
                        xq_num1 = float(input("Primary Value <> "))
                        xq_num2 = float(input("To-The-Power Value <> "))
                        sum = xq(xq_num1, xq_num2)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        xq_num2 = float(input("To-The-Power Value <> "))
                        sum = xq(math_mem, xq_num2)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "cube" or math_command == "CUBE"):

                def cube(x):
                    return x ** 3
                
                if math_mem == 0:

                    try:
                        cube_input = float(input("Value <> "))
                        sum = cube(cube_input)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        sum = cube(math_mem)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "sq" or math_command == "SQ"):

                def sq(x):
                    return x ** 2
                
                if math_mem == 0:

                    try:
                        sq_input = float(input("Value <> "))
                        sum = sq(sq_input)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        sum = sq(math_mem)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "mem" or math_command == "MEM"):
                
                if math_mem == 0:
                    print("\u001b[32mMathematical memory is empty!\u001b[0m")

                else:
                    print("Stored value = \u001b[32m" + str(math_mem) + "\u001b[0m")

            elif (math_command == "memcls" or math_command == "MEMCLS"):
                math_mem -= math_mem
                print("\u001b[32mCleared math memory!\u001b[0m")

            elif (math_command == "cls" or math_command == "CLS"):
                os.system('cls')

            elif (math_command == "add" or math_command == "ADD"):

                def add(x, y):
                    return x + y

                if math_mem == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = add(num1, num2)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        num1 = float(input("Value <> "))
                        sum = add(math_mem, num1)
                        

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "sub" or math_command == "SUB"):

                def sub(x, y):
                    return x - y

                if math_mem == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = sub(num1, num2)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        num1 = float(input("Value <> "))
                        sum = sub(math_mem, num1)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "div" or math_command == "DIV"):

                def div(x, y):
                    return x / y

                if math_mem == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = div(num1, num2)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        num1 = float(input("Value <> "))
                        sum = div(math_mem, num1)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            elif (math_command == "multi" or math_command == "MULTI"):

                def multi(x, y):
                    return x * y

                if math_mem == 0:

                    try:
                        num1 = float(input("Value 1 <> "))
                        num2 = float(input("Value 2 <> "))
                        sum = multi(num1, num2)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Added to memory)")

                else:

                    try:
                        print("Using previous memory result for main value.")
                        num1 = float(input("Value <> "))
                        sum = multi(math_mem, num1)

                    except OverflowError:
                        print("\u001b[31mResult too large to solve!\u001b[0m")

                    except ValueError:
                        print("\u001b[31mValue invalid! Try again with a valid number.\u001b[0m")

                    else:
                        math_mem -= math_mem
                        math_mem += sum
                        print("Result = \u001b[32m" + str(sum) + "\u001b[0m (Refreshed memory)")

            else:
                print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")

    elif (user_command == "speak" or user_command == "SPEAK"):
        speechtext = input("\u001b[0mText to speak: ")
        S.Speak(speechtext)

    elif (user_command == "clock" or user_command == "CLOCK"):
        now = datetime.now()
        date_time = now.strftime("\u001b[0mDate: " + "%d/%m/%Y" + " | Time: " + "%H:%M:%S")
        print(date_time)

    elif (user_command == "web" or user_command == "WEB"):
        print("\u001b[0mExecuted web console! Type 'help' to show executable commands.")

        while True:
            webcommand = input("\nWeb> ")

            if (webcommand == "help" or webcommand == "HELP"):
                print("\n\nCLS      Refreshes the screen.")
                print("CSITE    Opens a custom webpage given by user.")
                print("EXIT     Closes web console.")
                print("SEARCH   Searches the web for a particular object given by user.")
                print("SITES    Shows a list of popular sites to open.\n")

            elif (webcommand == "csite" or webcommand == "CSITE"):
                website = input("Website link / URL: ")
                webbrowser.open(website, new=2)
                print("\u001b[32mWeb page opened successfully!\u001b[0m")
                break

            elif (webcommand == "search" or webcommand == "SEARCH"):
                search_topic = input("Search for: ")
                website = "https://www.google.com/search?q=" + search_topic
                webbrowser.open(website, new=2)
                print("Showing results found for \u001b[32m'" + search_topic + "'\u001b[0m.")

            elif (webcommand == "exit" or webcommand == "EXIT"):
                break

            elif (webcommand == "cls" or webcommand == "CLS"):
                os.system('cls')

            elif (webcommand == "sites" or webcommand == "SITES"):

                print("\n\nEnter site number in-line to open.\n")
                print("1  YouTube")
                print("2  Facebook")
                print("3  Wikipedia")
                print("4  Google")
                print("5  LinkedIn")
                print("6  GitHub\n\n")

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
        dir_name = input("\u001b[0mDirectory name: ")
        os.mkdir(dir_name)
        print("\u001b[32mDirectory created successfully!\u001b[0m")

    elif (user_command == "del" or user_command == "DEL"):

        while True:
            filetype = input("\u001b[0mFile type ('help' for commands): ")

            if (filetype == "help" or filetype == "HELP"):
                print("\n\nCLS    Refreshes the screen.")
                print("DIR    Assigns file type as directory.")
                print("DOC    Assigns file type as document.")
                print("EXIT   Returns to home.\n\n")

            elif (filetype == "cls" or filetype == "CLS"):
                os.system('cls')

            elif (filetype == "dir" or filetype == "DIR"):
                mydir = input("Directory path: ")

                try:
                    shutil.rmtree(mydir)
                    print("\u001b[32mDeleted directory successfully!\u001b[0m")
                    break

                except OSError:
                    print("\u001b[31mDirectory not found, try again.\u001b[0m\n")

            elif (filetype == "doc" or filetype == "DOC"):
                mydoc = input("File path: ")

                if os.path.isfile(mydoc):
                    os.remove(mydoc)
                    print("\u001b[32mDeleted file successfully!\u001b[0m")
                    break

                else:
                    print("\u001b[31mFile not found, try again.\u001b[0m\n")

            elif (filetype == "exit" or filetype == "EXIT"):
                break

            else:
                print("\u001b[31mFile type / command not recognized! Type 'help' to show executable commands.\u001b[0m")

    elif (user_command == "sys" or user_command == "SYS"):
        print("\u001b[0m\n\nDevice platform  : \u001b[32m" + device_platform + "\u001b[0m")
        print("Chipset          : \u001b[32m" + processor + "\u001b[0m")
        print("Operating system : \u001b[32m" + operating_system + "\u001b[0m")
        print("Build            : \u001b[32m" + build + "\u001b[0m\n")

    elif (user_command == "vdl" or user_command == "VDL"):

        def dwl_vid():
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([vidmain])

        vidformat = input("\u001b[0mDownload as (audio/video/exit): ")

        if (vidformat == "video" or vidformat == "VIDEO"):

            try:
                ydl_opts = {}
                vidlink = input("Video link / URL: ")
                vidmain = vidlink.strip()
                dwl_vid()

            except:
                print("\u001b[31mInvalid link! Try again with a valid video link / URL.\u001b[0m\n")

            else:
                print("\u001b[32mVideo downloaded successfully!\u001b[0m")
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

                vidlink = input("Video link / URL: ")
                vidmain = vidlink.strip()
                dwl_vid()
                
            except:
                print("\u001b[31mInvalid link! Try again with a valid video link / URL.\u001b[0m\n")

            else:
                print("\u001b[32mVideo successfully downloaded as audio.\u001b[0m")
                break

        elif (vidformat == "exit" or vidformat == "EXIT"):
            break

        else:
            print("\u001b[31mFormat not recognised! Type either video or audio for format selection.\u001b[0m\n")

    else:
        print("\u001b[31mWhoa! Command not found. Type 'help' to show executable commands.\u001b[0m")