import tkinter as tk
from tkinter import ttk

def greet():
    print(f"Hello, {user_name.get() or 'World'}!")
#    print(f"Hello, {'World' or user_name.get()}!")

root = tk.Tk()

user_name = tk.StringVar()

name_label = tk.Label(root, text="Name: ")
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()


greet_button = ttk.Button(root, text="Greet", padding=(30,10), command=greet)
greet_button.pack(side="right")

#ttk.Label(root, text="Hello, World!", padding=(30,10)).pack(side="left")

quit_button = ttk.Button(root, text="Quit", padding=(30,10),command=root.destroy)
quit_button.pack(side="left")

root.mainloop()


