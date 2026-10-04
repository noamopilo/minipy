import subprocess
import spotdl
import shutil
from pathlib import Path

downloads_folder = Path.home() / "Downloads"

def spotify_download(url):
    command = ["spotdl", url, "--output", downloads_folder]
    
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Succesfully downloaded and saved in your downloads folder.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error ocurred: {e}")

url = input("Enter a spotify URL: ").strip()
spotify_download(url)