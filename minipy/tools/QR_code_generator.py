import qrcode
from pathlib import Path
import tkinter as tk
from PIL import ImageTk

data = input("Enter the text or URL you want the QR-code to redirect to: ").strip()
while not data:
    data = input("Input cannot be empty, please enter text or URL: ").strip()
    


def generate_qr():
    img = qrcode.make(data)
    
    root = tk.Tk()
    root.title("Your QR")
    
    tk_img = ImageTk.PhotoImage(img)
    
    label = tk.Label(root, image=tk_img)
    label.pack(padx=10, pady=10)
    
    root.update()
    
    choice = input("Do you want to save the QR-code to your Downloads folder? (Y/N): ").strip().lower()
    
    if choice =="y":
        fileName = input("What should the file be named? (without extension): ").strip()
        
        while not fileName:
            fileName = input("Input cannot be empty, please enter a file name: ").strip()   
                 
        downloads_folder = Path.home() / "Downloads"
        img.save(downloads_folder / f"{fileName}.png")
        print(f"QR-code saved in Downloads as: {fileName}.png")
    else:
        print("QR-code not saved")

    print("Thank you for using!")
    root.destroy()
    
        

generate_qr()