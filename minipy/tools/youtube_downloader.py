from yt_dlp import YoutubeDL
import os
from pathlib import Path

downloads_path = Path.home() / "Downloads"

ydl_opts =  {
    'outtmpl': str(downloads_path / '%(title)s.%(ext)s'),
    'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
}

link = input("Input the url of the youtube video you want to download: ").strip()
def download_youtube():
    while True:
        print("\nWhat do you want to download?")
        print("1. Video (mp4)")
        print("2. Only Audio (mp3)")
        choice = input("Make a choice: (1 or 2): ").strip()

        if choice == "1":
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
            print("\nVideo downloading...")
            break
        elif choice =="2":
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
            break
        else:
            print("Not valid choice. Please input a valid choice.")
    browsers = ['chrome', 'edge', 'firefox', 'brave', 'safari']
    download_success = False  
      
    for browser in browsers:
        try:
            ydl_opts['cookiesfrombrowser'] = (browser,)
            ydl_opts['cookiefile_ignore_lock'] = True
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            
            download_success = True
            break
        except Exception:
            continue
        
    if not download_success:
        try:
            ydl_opts.pop('cookiesfrombrowser', None)
                
            with YoutubeDL as ydl:
                ydl.download([link])
            download_success = True
        except Exception as e:
            print(f"\nError: {e}")
    
    if download_success:
        print("\Succecfully downloaded the video in your Downloads folder.")

if __name__ == "__main__":
    download_youtube()

