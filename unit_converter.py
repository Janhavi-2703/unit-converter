from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu, messagebox, Text, Scrollbar, Menu, Toplevel

def convert_units():
    try:
        value = float(entry.get())
        unit_from = from_unit.get()
        unit_to = to_unit.get()

        # Conversion logic
        conversions = {
            "meters": {"kilometers": value / 1000},
            "kilometers": {"meters": value * 1000},
            "grams": {"kilograms": value / 1000},
            "kilograms": {"grams": value * 1000},
            "celsius": {"fahrenheit": (value * 9 / 5) + 32},
            "fahrenheit": {"celsius": (value - 32) * 5 / 9},
        }

        if unit_from in conversions and unit_to in conversions[unit_from]:
            result_value = conversions[unit_from][unit_to]
            result.set(f"{value} {unit_from} = {result_value:.2f} {unit_to}")
            log_conversion(value, unit_from, result_value, unit_to)
        else:
            messagebox.showerror("Error", "Invalid or unsupported conversion selected!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def log_conversion(value, unit_from, result_value, unit_to):
    history_box.insert("end", f"{value} {unit_from} = {result_value:.2f} {unit_to}\n")
    history_box.see("end")

def clear_fields():
    entry.delete(0, "end")
    result.set("")

def save_history():
    with open("conversion_history.txt", "w") as file:
        file.write(history_box.get("1.0", "end"))
    messagebox.showinfo("Saved", "Conversion history saved to 'conversion_history.txt'")

def clear_history():
    history_box.delete("1.0", "end")

def show_help():
    help_window = Toplevel(root)
    help_window.title("Help")
    help_window.geometry("400x300")
    Label(
        help_window,
        text=(
            "Unit Converter Help:\n\n"
            "1. Enter a value in the input field.\n"
            "2. Select the units to convert from and to.\n"
            "3. Click 'Convert' to see the result.\n"
            "4. View the history below or save it to a file.\n"
            "5. Only compatible units can be converted."
        ),
        font=("Times New Roman", 12),
        justify="left",
    ).pack(pady=10, padx=10)

def apply_theme(theme):
    if theme == "Light":
        root.configure(bg="#f0f8ff")
    elif theme == "Dark":
        root.configure(bg="#2e2e2e")
        for widget in root.winfo_children():
            widget.configure(bg="#2e2e2e", fg="white")

root = Tk()
root.title("Unit Converter")
root.geometry("500x600")
root.configure(bg="#f0f8ff")

# Input Value
Label(root, text="Value:", font=("Times New Roman", 12)).pack(pady=5)
entry = Entry(root, font=("Times New Roman", 12))
entry.pack(pady=5)

# Units Selection
units = ["meters", "kilometers", "grams", "kilograms", "celsius", "fahrenheit"]
from_unit = StringVar(value=units[0])
to_unit = StringVar(value=units[1])

Label(root, text="From:", font=("Times New Roman", 12)).pack(pady=5)
OptionMenu(root, from_unit, *units).pack(pady=5)

Label(root, text="To:", font=("Times New Roman", 12)).pack(pady=5)
OptionMenu(root, to_unit, *units).pack(pady=5)

# Convert Button
Button(root, text="Convert", command=convert_units, bg="#4682b4", fg="white", font=("Times New Roman", 12)).pack(pady=10)

# Result Display
result = StringVar()
Label(root, textvariable=result, font=("Times New Roman", 14, "bold"), fg="green").pack(pady=10)

# History Section
Label(root, text="Conversion History:", font=("Times New Roman", 12)).pack(pady=5)

history_frame = Scrollbar(root)
history_frame.pack(side="right", fill="y")

history_box = Text(root, height=10, width=50, font=("Times New Roman", 10))
history_box.pack(pady=5)
history_frame.config(command=history_box.yview)
history_box.config(yscrollcommand=history_frame.set)

# Buttons for Extra Features
Button(root, text="Clear Fields", command=clear_fields, bg="#4682b4", fg="white", font=("Times New Roman", 12)).pack(pady=5)
Button(root, text="Save History", command=save_history, bg="#4682b4", fg="white", font=("Times New Roman", 12)).pack(pady=5)
Button(root, text="Clear History", command=clear_history, bg="#4682b4", fg="white", font=("Times New Roman", 12)).pack(pady=5)

# Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save History", command=save_history)
file_menu.add_command(label="Clear History", command=clear_history)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help", command=show_help)
menu_bar.add_cascade(label="Help", menu=help_menu)

theme_menu = Menu(menu_bar, tearoff=0)
theme_menu.add_command(label="Light", command=lambda: apply_theme("Light"))
theme_menu.add_command(label="Dark", command=lambda: apply_theme("Dark"))
menu_bar.add_cascade(label="Themes", menu=theme_menu)

root.mainloop()
