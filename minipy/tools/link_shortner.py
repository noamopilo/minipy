import requests
import os
from dotenv import load_dotenv, set_key
from pathlib import Path

ENV_PATH = Path(__file__).resolve().parent / ".env"
BASE_URL = 'https://cutt.ly/api/api.php'


def config():
    if not ENV_PATH.exists():
        ENV_PATH.touch()
    
    load_dotenv(dotenv_path=ENV_PATH)
    
    api_key = os.getenv("CUTTLY_API_KEY")
    
    if not api_key:
        print("This is the first time you're using this tool.")
        print("We're gonna do some configuration.\n")
        print("Read the instructions in the \033]8;;https://github.com/noamopilo/minipy/blob/main/README.md\033\\README\033]8;;\033\\ on how to create a cuttly API key.")
        
        if not api_key:
            api_key = input("Input your cuttly API key: ").strip()
            set_key(str(ENV_PATH), "CUTTLY_API_KEY", api_key)
        
        print("Configuration succesfull!\n")
        load_dotenv(dotenv_path=ENV_PATH)
        
    return os.getenv("CUTTLY_API_KEY")

def shorten_url(long_url, alias, API_KEY):
    params = {
        'key': API_KEY,
        'short': long_url,
        'name': alias
    }
    
    request = requests.get(BASE_URL, params=params)
    data = request.json()
    
    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        print('Title: ', title)
        print('Short url: ', short_link)
    except:
        status = data['url']['status']
        if status == 3:
            status = 'Alias is already taken'
        print('Error status: ', status)

if __name__ == "__main__":
    API_KEY = config()
    long_url = input("What is the long url you wnat to shorten?: ")
    alias = input("What is the alias you want for yout short url? (https://cutt.ly/alias): ")
    shorten_url(long_url, alias, API_KEY)