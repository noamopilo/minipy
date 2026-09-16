from random import randint

while True:
    responce = input("Roll the dice? (Y/N): ").lower()
    if responce == "y":
        print(randint(1,6))
    elif responce =="n":
        print("Bye! thanks for using.")
        break
    else:
        print("Please choose an option (Y/N): ")
    

