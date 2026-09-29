import pyautogui
import keyboard
import os
from datetime import datetime
from pathlib import Path

downloads_path = Path.home() / "Downloads"

def main():
    img = pyautogui.screenshot()
    filename = datetime.now().strftime("screenshot_%Y-%m-%d_%H-%M-%S.png")
    fullpath = os.path.join(downloads_path, filename)
    img.save(filename)
    print(f"Screenshot saved succesfully as {filename} in your downloads folder.")

print("Press CTRL + SHIFT + S to take a screenshot, Press ESC to exit.")
keyboard.add_hotkey('ctrl+shift+s', main)
keyboard.wait('esc')
print("Closing app...")