# extensions
# - Work with Rich and make a cool graphical interface

import subprocess
from pathlib import Path
import inquirer
import sys
import os
import time
from inquirer.themes import Default
import blessed

term = blessed.Terminal()

SRC = Path(__file__).parent

BANNER = "\033[0;38;5;72;49m" + r"""
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
 |  __  __   ___   _   _   ___   ____   __   __  |
|  |  \/  | |_ _| | \ | | |_ _| |  _ \  \ \ / /   |
|  | |\/| |/ | | \|  \| |/ | | \| |_) | /\ V /    |
|  |_|  |_| |___| |_| \_| |___| | .__/    | |     |
 |                              |_|       |_|    |
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

""" + "\033[0m"

class MyTheme(Default):
    def __init__(self):
        super().__init__()
        self.List.selection_cursor = "->"
        self.List.selection_color = term.color(241)
def main():
    while True:
        clear_screen()
        print(BANNER)
            
        category = ask("\033[1;38;5;180;49mChoose a category\033[0m", 
                    categorys() + ["\033[1;31mStop\033[0m"],)
        if category == "\033[1;31mStop\033[0m":
            clear_screen()
            print("Bye!")
            break
            
        clear_screen()
        print(BANNER)
            
        project = ask(
            f"\033[1;38;5;180;49mChoose a project in {category}\033[0m",
            projects(category) + ["\033[1;33mBack\033[0m"],
        )
            
        if project != "\033[1;33mBack\033[0m":
            start(category, project)

                
        if project == "\033[1;33mBack\033[0m":
            continue

def categorys():
    return sorted(file.name for file in SRC.iterdir() if file.is_dir() and file.name != "venv" and file.name != "__pycache__" and not file.name.startswith("."))

def projects(category):
    return sorted(
        file.stem.replace("_", " ")
        for file in (SRC / category).iterdir()
        if file.is_file() and file.suffix == ".py"
    )

def ask(text, choices):
    answer = inquirer.prompt([
        inquirer.List("choice", message=text, choices=choices)
    ], theme=MyTheme())
    return answer["choice"]

def start(category, name):
    pad = SRC / category / f"{name.replace(' ', '_')}.py"
    clear_screen()
    
    clean_name = name.replace("_", " ").upper()
    
    print("\033[1;36m-------------------------------------------------------------------------")
    print(f"--> OPEN APP: {clean_name}  , Close app with Ctrl+C")
    print("----------------------------------------------------------------------------\033[0m")
    print()
    
    try:
        subprocess.run([sys.executable, str(pad)], check=True)
        print()
        print("---------------------------------------------------")
        input("Press Enter to return to the menu...")
    except (KeyboardInterrupt, subprocess.CalledProcessError):
        #clear_screen()
        print("\n\nApp closed with Ctrl+C. Returning to main menu...")
        time.sleep(5)
    

    


def clear_screen():
    if os.name =='nt':
        subprocess.run(["cmd", "/c", "cls"])
    else:
        subprocess.run(["clear"])
    
if __name__ == "__main__":
    main()