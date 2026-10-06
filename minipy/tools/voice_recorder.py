import sys
import wave
import time
import threading
import tkinter as tk
from pathlib import Path

try:
    import pyaudio
except ImportError:
    sys.exit("pyaudio is not installed. Run this first: pip install minipy-tools[audio]")

downloads_folder = Path.home() / "Downloads"

class Recorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.button = tk.Button(text="🎤", font=("Arial", 120, "bold"), command=self.click_handler)
        self.button.pack()
        self.label = tk.Label(text="00:00:00", font=("Consolas", 80))
        self.label.pack()
        self.recording = False
        self.root.mainloop()
        
    def click_handler(self):
        if self.recording:
            self.recording = False
            self.button.config(fg="black")
        else:
            self.recording = True
            self.button.config(fg="red")
            threading.Thread(target=self.record).start()
    
    def record(self):
        audio = pyaudio.PyAudio()
        sample_width = audio.get_sample_width(pyaudio.paInt16)
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []
        start = time.time()
        
        while self.recording:
            data = stream.read(1024, exception_on_overflow=False)
            frames.append(data)
            passed = time.time() - start
            secs = passed % 60
            mins = passed // 60
            hours = mins // 60
            self.label.config(text=f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")
            
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        exists = True
        i = 1
        while exists:
            full_path = downloads_folder / f"recording{i}.wav"
            if not full_path.exists():
                break
            i += 1
        
        sound_file = wave.open(str(full_path), "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(sample_width)
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()
        print(f"Recording saved in your Downloads as: recording{i}.wav")
                

Recorder()