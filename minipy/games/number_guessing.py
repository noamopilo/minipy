from random import randint

number = randint(1, 100)

while True:
    answer = input("Guess the number between 1 and 100: ")
    if answer.isdigit():
        if int(answer) < number:
            print("Too low!")
        elif int(answer) > number:
            print("Too high!")
        elif int(answer) == number:
            print("Congratulations you guessed the number!")
            print(f"The number was: {number}")
            break
    else:
        print("Please enter a valid number")