# extensions
# - Work with Rich and make a cool graphical interface

import subprocess
from pathlib import Path
import inquirer
import sys
import os
import time

SRC = Path(__file__).parent

BANNER = r"""
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
 |  __  __   ___   _   _   ___   ____   __   __  |
|  |  \/  | |_ _| | \ | | |_ _| |  _ \  \ \ / /   |
|  | |\/| |/ | | \|  \| |/ | | \| |_) | /\ V /    |
|  |_|  |_| |___| |_| \_| |___| | .__/    | |     |
 |                              |_|       |_|    |
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

"""
def main():
    while True:
        clear_screen()
        print(BANNER)
            
        category = ask("Choose a category: ", 
                    categorys() + ["\033[1;31mStop\033[0m"],)
        if category == "\033[1;31mStop\033[0m":
            clear_screen()
            print("Bye!")
            break
            
        clear_screen()
        print(BANNER)
            
        project = ask(
            f"Choose a project in {category}",
            projects(category) + ["\033[1;33mBack\033[0m"],
        )
            
        if project != "\033[1;33mBack\033[0m":
            start(category, project)

                
        if project == "\033[1;33mBack\033[0m":
            continue

def categorys():
    return sorted(file.name for file in SRC.iterdir() if file.is_dir() and file.name != "venv" and not file.name.startswith("."))

def projects(category):
    return sorted(
        file.stem
        for file in (SRC / category).iterdir()
        if file.is_file() and file.suffix == ".py"
    )

def ask(text, choices):
    answer = inquirer.prompt([
        inquirer.List("choice", message=text, choices=choices)
    ])
    return answer["choice"]

def start(category, name):
    pad = SRC / category / f"{name}.py"
    clear_screen()
    
    clean_name = name.replace("_", " ").upper()
    
    print("\033[1;36m---------------------------------------------------")
    print(f"--> OPEN APP: {clean_name}  , Close app with Ctrl+C")
    print("---------------------------------------------------\033[0m")
    print()
    
    try:
        subprocess.run([sys.executable, str(pad)], check=True)
        print()
        print("---------------------------------------------------")
        input("Press Enter to return to the menu...")
    except (KeyboardInterrupt, subprocess.CalledProcessError):
        clear_screen()
        print("\n\nApp closed with Ctrl+C. Returning to main menu...")
        time.sleep(1.5)
    

    


def clear_screen():
    if os.name =='nt':
        subprocess.run(["cmd", "/c", "cls"])
    else:
        subprocess.run(["clear"])
    
if __name__ == "__main__":
    main()