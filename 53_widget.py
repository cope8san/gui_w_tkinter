import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry("600x400")
root.resizable(False,False)
root.title("ご挨拶")

#label = ttk.Label(root, text="こんにちは、世界", padding=20)


#label.config(font=("Meiryo", 20))

with open("logo.png", "rb") as f:
#    image = Image.open(f).resize((64,64))
    image = Image.open(f)
    image = image.convert("RGBA")  # Convert to a compatible format if needed

photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, text="Image with text.",image=photo, padding=5, compound="right")
label.pack()

label["image"] = photo
root.mainloop()
