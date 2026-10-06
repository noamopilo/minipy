import subprocess
from pathlib import Path
import sys

downloads_folder = Path.home() / "Downloads"

def spotify_download(url):
    command = [sys.executable, "-m", "spotdl", url, "--output", downloads_folder]
    
    try:
        result = subprocess.run(command, check=True, text=True)
        print("Succesfully downloaded and saved in your downloads folder.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error ocurred: {e}")

url = input("Enter a spotify URL: ").strip()
spotify_download(url)