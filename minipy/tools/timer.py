import time
from pathlib import Path
from playsound import playsound

my_time = int(input("Enter the time in seconds: ").strip())

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("!!!  TIME UP  !!!")
playsound(str(Path(__file__).resolve().parent.parent / "assets" / "alarm.mp3"))