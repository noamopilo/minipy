from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)

label = Label(root,  width=11,font=("calibri", 50, "bold"), background="cyan", foreground="black")

label.pack(expand=True, fill="both")

root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

time()

root.mainloop()