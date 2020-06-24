# Copyright (c) 2020 Anindya Shiddhartha
# Read the LICENSE and README.md file for more information.
# You are only allowed to make changes to the code if you have the license file of the project.
# This is the Python file for installing missing modules for the source code.
# Run it before executing main.py

import subprocess

import time

import os
def cls():
    os.system("clear")


while True:
    print()
    user_command = input("Start process? (yes or no): ")
    print()

    if user_command == "yes":
        print("Upgrading PIP if available...")
        subprocess.run("python -m pip install --upgrade pip", shell=True, check=True)
        print()

        print("Installing missing modules...")
        subprocess.run("python -m pip install pywin32", shell=True, check=True)
        subprocess.run("python -m pip install youtube-dl", shell=True, check=True)
        print()
        print("Process finished! Exiting window...")
        time.sleep(1)
        break

    elif user_command == "no":
        cls()
        print("Cleaning up...")

    else:
        print("Command not found!")

