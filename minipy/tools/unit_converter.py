import tkinter as tk
from tkinter import ttk

conversion_map = {
    "Miles" : {"Kilometers": lambda x: x * 1.60934},
    "Kilometers" : {"Miles": lambda x: x / 1.60934},
    "Pounds" : {"Kilograms": lambda x: x * 0.453592},
    "Kilograms" : {"Pounds": lambda x: x / 0.453592},
    "Inches" : {"Centimeters": lambda x: x * 2.54},
    "Centimeters" : {"Inches": lambda x: x / 2.54},
    "Fahrenheit" : {"Celsius": lambda x: (x - 32) * 5/9},
    "Celsius" : {"Fahrenheit": lambda x: (x * 9/5) + 32}
}

def update_to_units(event):
    selected_unit = unit_from_var.get()
    if selected_unit in conversion_map:
        combo_to["values"] = list(conversion_map[selected_unit].keys())
        combo_to.set("")
    else:
        combo_to["values"] = []
        combo_to.set("")

def convert():
    unit_from = unit_from_var.get()
    unit_to = unit_to_var.get()
    
    try:
        value = float(entry_value.get())
    except ValueError:
        label_result.config(text="Invalid input. Please enter a number.")
        return
        
    if unit_from in conversion_map and unit_to in conversion_map[unit_from]:
        result = conversion_map[unit_from][unit_to](value)
        label_result.config(text=f"{value} {unit_from} = {result:.2f} {unit_to}")
    
    else:
        label_result.config(text="Invalid conversion.")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x380")
root.configure(bg="#e5e5e5")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

border_frame = tk.Frame(root, background="#fca311")
border_frame.grid(row=0, column=0, sticky="nsew")

main_frame = tk.Frame(border_frame, background="#e5e5e5")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

label_value = ttk.Label(main_frame, text="Value", background="#e5e5e5")
label_value.pack(pady=5)
entry_value = ttk.Entry(main_frame, font=("Arial", 15))
entry_value.pack(pady=5)

label_from = ttk.Label(main_frame, text="Convert from:", background="#e5e5e5")
label_from.pack(pady=5)
unit_from_var = tk.StringVar()
combo_from = ttk.Combobox(main_frame, textvariable=unit_from_var, font=("Arial", 10))
combo_from["values"] = list(conversion_map.keys())
combo_from.bind("<<ComboboxSelected>>", update_to_units)
combo_from.pack(pady=5)

label_to = ttk.Label(main_frame, text="To:", background="#e5e5e5")
label_to.pack(pady=5)
unit_to_var = tk.StringVar()
combo_to = ttk.Combobox(main_frame, textvariable=unit_to_var, font=("Arial", 10))
combo_to.pack(pady=5)

button_convert = ttk.Button(main_frame, text="convert", command=convert, style="TButton")
button_convert.pack(pady=10)

label_result = ttk.Label(main_frame, text="", font=("Arial", 14), background="#e5e5e5", foreground="#14213d")
label_result.pack(pady=20)

root.mainloop()