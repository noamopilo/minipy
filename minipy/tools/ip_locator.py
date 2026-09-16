import requests
import os
from PIL import Image
from io import BytesIO
from tkinter import Tk, Label
from PIL import ImageTk
from dotenv import load_dotenv, set_key
from pathlib import Path

CONFIG_DIR = Path.home() / ".minipy"
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
ENV_PATH = CONFIG_DIR / ".env"
BASE_URL = 'https://ip-intelligence.abstractapi.com/v1/'


def show_img(flag_image_url):
    response = requests.get(flag_image_url)
    img = Image.open(BytesIO(response.content))
    
    root = Tk()
    root.title("Flag")
    
    photo = ImageTk.PhotoImage(img)
    label = Label(root, image=photo)
    label.pack()
    
    root.mainloop()
    
    

def config():
    if not ENV_PATH.exists():
        ENV_PATH.touch()
    
    load_dotenv(dotenv_path=ENV_PATH)
    
    api_key = os.getenv("Abstract_IP_API_key")
    
    if not api_key:
        print("This is the first time you're using this tool.")
        print("We're gonna do some configuration.\n")
        print("Read the instruction in the \033]8;;https://github.com/noamopilo/minipy/blob/main/README.md\033\\README\033]8;;\033\\ on how to create a Abstract ip API key")
        api_key = input("Input you Abstract ip API key: ").strip()
        set_key(str(ENV_PATH), "Abstract_IP_API_key", api_key)
        
        print("Configuration succesfull!\n")
        load_dotenv(dotenv_path=ENV_PATH)
    
    return os.getenv("Abstract_IP_API_key")

def locate_ip():
    API_KEY = config()
    ip_address = input("What is the public IP address you want to loacte?: ")
    params = {
        "api_key": API_KEY,
        "ip_address": ip_address
    }
    
    request = requests.get(BASE_URL, params=params)
    data = request.json()
    
    try:
        country = data['location']['country']
        country_code = data['location']['country_code']
        city = data['location']['city']
        continent = data['location']['continent']
        local_time = data['timezone']['local_time']
        flag_image_url = data['flag']['png']
        
        print(f"This IP address ({ip_address}) is located in {city}, {country}({country_code}), {continent}")
        print(f"Local time at location: {local_time}")
        answer = input("Do you want to see the flag of this country? (Y/N): ").lower().strip()
        
        if answer == "y":
            print("Image opening in new window...")
            show_img(flag_image_url)
    except:
        print("Something went wrong, please check your API key, IP adress or Internet connection and try again.")

locate_ip()