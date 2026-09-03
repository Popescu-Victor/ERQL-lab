import argparse
from curses import echo
from os import name
from py_compile import main
import selenium
import dotenv
import pandas as pd
import keyring
import subprocess
import os


parser = argparse.ArgumentParser(description="My CLI tool")
parser.add_argument("login", help="Storing encrypted login credentials locally.")

def login_to_env():
    # Implement the logic to log in to the environment using Selenium
    pass

def str_finder(folder_path, target_string):
    for i in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, i)):
            with open(os.path.join(folder_path, i), 'r') as file:
                if target_string in file.read():
                    print(f"Found '{target_string}' in {i}")

def grepper(folder_path, target_string):
    for file in os.listdir(folder_path):
        result = subprocess.run(['powershell', '-Command', 'Get-Process' , target_string, os.path.join(folder_path, file)], capture_output=True, text=True)
    print(result.stdout)

def main():
    args = parser.parse_args()
    pass

if __name__ == "__main__":
    main()