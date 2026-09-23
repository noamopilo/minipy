import requests
from pathlib import Path
import os
from dotenv import load_dotenv, set_key

CONFIG_DIR = Path.home() / ".minipy"
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
ENV_PATH = CONFIG_DIR / ".env"
BASE_URL = ""

def config():
    if not ENV_PATH.exists():
        ENV_PATH.touch()
    
    load_dotenv(dotenv_path=ENV_PATH)
    
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    
    if not api_key:
        print("This is the first time you're using this tool.")
        print("We're gonna do some configuration.\n")
        print("Read the instructions in the \033]8;;https://github.com/noamopilo/minipy/blob/main/README.md\033\\README\033]8;;\033\\ on how to create a Open Weather Map API key")
        
        api_key = input("Input your Open Weather Map API key: ").strip()
        set_key(str(ENV_PATH), "OPEN_WEATHER_API_KEY", api_key)
        
        print("Configuration succesfull!\n")
        load_dotenv(dotenv_path=ENV_PATH)
        
    return os.getenv("OPEN_WEATHER_API_KEY")

api_key = config()

def weather():
    city = input("Enter a city: ").strip()
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")
    
    weather = weather_data.json()["weather"][0]["main"]
    description = weather_data.json()["weather"][0]["description"]
    temp = weather_data.json()["main"]["temp"]
    feels_like = weather_data.json()["main"]["feels_like"]
    
    print(f"\nWeather in {city}: ")
    print(f"Weather: {weather}, {description}")
    print(f"Temperature: {temp}°C, feels like {feels_like}°C")
    

weather()