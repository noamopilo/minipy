import requests
import json


def get_fun_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    
    response = requests.get(url)
    data = json.loads(response.text)
    
    fun_fact = data["text"]
    
    return fun_fact

while True:
    answer = input("Do you want a fun fact? (Y/N): ").strip().lower()
    print("\n")
    if answer == "y":
        print(get_fun_fact())
        print("\n")
    elif answer == "n":
        break




    
    