import tkinter as tk
from tkinter import ttk
import random, string

def generate_password(length, include_uppercase, include_digits, include_special_chars):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button_clicked():
    length = length_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_special_chars = special_chars_var.get()
    password = generate_password(length, include_uppercase, include_digits, include_special_chars)
    password_var.set(password)

def copy():
    window.clipboard_clear()
    window.clipboard_append(password_entry.get())

# Create main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x350+200+300")

# Create and pack widgets
length_label = ttk.Label(window, text="Password Length:")
length_label.pack(pady=5)

length_var = tk.IntVar(None,8,None) # Default
length_entry = ttk.Entry(window, textvariable=length_var)
length_entry.pack(pady=5)

check_frame = tk.Frame(window, width=300, height=130)
check_frame.pack()
uppercase_var = tk.BooleanVar()
uppercase_checkbox = ttk.Checkbutton(check_frame, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.pack(fill="x",pady=5)
uppercase_var.set(True)

digits_var = tk.BooleanVar()
digits_checkbox = ttk.Checkbutton(check_frame, text="Include Digits", variable=digits_var)
digits_checkbox.pack(fill="x",pady=5)
digits_var.set(True)

special_chars_var = tk.BooleanVar()
special_chars_checkbox = ttk.Checkbutton(check_frame, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.pack(fill="x",pady=5)
special_chars_var.set(True)

generate_button = ttk.Button(window, text="Generate", command=generate_password_button_clicked)
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_label = ttk.Label(window, text="Generated Password:")
password_label.pack(pady=5)

password_entry = ttk.Entry(window, textvariable=password_var, state="readonly")
password_entry.pack(pady=5)

copy_button = ttk.Button(window, text="COPY", command = copy)
copy_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
