import subprocess
from pathlib import Path
import sys

download_folder = Path.home() / "Downloads"

def youtube_download(url):
    command = [
        sys.executable,
        "-m",
        "yt_dlp",
        "-f", "bestvideo+bestaudio",
        "--merge-output-format", "mp4",
        "-o", str(download_folder / "%(title)s.%(ext)s"),
        url
    ]
    
    try:
        result = subprocess.run(command, check=True, text=True)
        print("Succesfully downloaded in you downloads folder.")
    except subprocess.CalledProcessError as e:
        print(f"An error has ocurred: {e.returncode}")

url = input("Enter a youtube URL: ").strip()
youtube_download(url)