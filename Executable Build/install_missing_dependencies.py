# This code is licensed under Apache License 2.0, so read the LICENSE file before going any further.
# You are allowed to read, modify and distribute this code.
# You are not allowed to make changes to it's name and claim it as yours!

import time
import subprocess

print("This tool will allow you to install missing dependencies for the executable build of BlastShell.")

while True:
    print()
    user_input = input("Start? (type yes or no)")
    print()

    if user_input == "yes":
        print("Upgrading PIP...")
        print()
        subprocess.run("python -m pip install --upgrade pip", shell=True, check=True)
        print()
        print("Checking for missing dependencies...")
        print()
        subprocess.run("python -m pip install ffmpeg-python", shell=True, check=True)
        subprocess.run("python -m pip install youtube-dl", shell=True, check=True)
        subprocess.run("python -m pip install pywin32", shell=True, check=True)
        print()
        print("Closing in 3 seconds...")
        time.sleep(3)
        break

    elif user_input == "no":
        print("Closing in 3 seconds...")
        time.sleep(3)
        break

    else:
        print("Command not found.")
