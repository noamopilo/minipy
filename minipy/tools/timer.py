import time
from pathlib import Path
import pygame

alarm = str(Path(__file__).resolve().parent.parent / "assets" / "alarm.mp3")

my_time = int(input("Enter the time in seconds: ").strip())

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("!!!  TIME UP  !!!")
pygame.mixer.init()
sound = pygame.mixer.Sound(alarm)
sound.play()
while pygame.mixer.get_busy():
    time.sleep(0.1)