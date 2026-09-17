import random
import string

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Should your password include uppercas letter? (Y/N): ").strip().lower()
    include_special = input("Should you password include special characters? (Y/N): ").strip().lower()
    include_digits = input("Should your password include digits? (Y/N): ").strip().lower()
    
    if length < 4:
        print("Password length must be at least 4 characters.")
        return
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "y" else ""
    special = string.punctuation if include_special == "y" else ""
    digits = string.digits if include_digits =="y" else ""
    all_characters = lower + upper + special + digits
    
    required_characters = []
    if include_uppercase =="y":
        required_characters.append(random.choice(upper))
    if include_special =="y":
        required_characters.append(random.choice(special))
    if include_digits =="y":
        required_characters.append(random.choice(digits))
    
    remaining_length = length - len(required_characters)
    password = required_characters
    
    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)
    
    random.shuffle(password)
    str_password = "".join(password)
    return str_password

password = generate_password()
print(f"This is your password: {password}")