# extension:
# - multi receiver email system
# - beginning menu (send email, configuration, send multiple emails)


import os
import click
import smtplib
from pathlib import Path
from email.message import EmailMessage
from dotenv import load_dotenv, set_key

ENV_PATH = Path(__file__).resolve().parent / ".env"

def config():
    if not ENV_PATH.exists():
        ENV_PATH.touch()
        
    load_dotenv(dotenv_path=ENV_PATH)
    
    password = os.getenv("GOOGLE_APP_PASS")
    email = os.getenv("SENDER_EMAIL")

    if not password or not email:
        print("This is the first time you use this tool.")
        print("We're gonna do the configuration.\n")
        print("Read the instructions in the \033]8;;https://github.com/noamopilo/minipy/blob/main/README.md\033\\README\033]8;;\033\\ on how to create a Google App Password.")
        
        if not email:
            email = input("Input your Gmail-adress: ").strip()
            set_key(str(ENV_PATH), "SENDER_EMAIL", email)
            
        if not password:
            password = input("Input your Google App Password: ").strip()
            set_key(str(ENV_PATH), "GOOGLE_APP_PASS", password)
        
        print("Configuration succesfull!\n")
        
        load_dotenv(dotenv_path=ENV_PATH)
        
    return os.getenv("SENDER_EMAIL"), os.getenv("GOOGLE_APP_PASS")

def get_multiline_input_editor():
    instruction_text = "# Type your message above. Save the file and close it to send."
    message = click.edit(f"\n\n{instruction_text}")
    
    if message:
        good_message = message.replace(instruction_text, "").strip()
        return good_message
    return ""

def send_email(sender, password, receiver, subject, message):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    
    msg.set_content(message)
    
    print("\n ***Sending email...")
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        print("Email sent! --> ")
    except:
        print(f"Failed to send email. Error: {Exception}")
    

if __name__ == "__main__":
    user_email, user_password = config()
    print(f"User is: {user_email}")
    receiver = input("Who do you want to send an email to?: ")
    subject = input("What is the subject of the email?: ")
    action = input("Type 'E' to open the editor: ").strip().lower()
    if action == "e":
        print("Editor is opening...")
        message = get_multiline_input_editor()
   
        if not message.strip():
            print("Message is empty. Sending canceled!")
        else:
            print("\n--- Your message ---")
            print(message)
            print("--------------------")
            send_email(user_email, user_password, receiver, subject, message)
            