import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

rectangle_1 = tk.Label(root, text="Rect1", bg="green", fg="white")
rectangle_1.pack(side="left",ipadx=10, ipady=10,fill="both",expand=True)

rectangle_2 = tk.Label(root, text="Rect2", bg="red", fg="white")
rectangle_2.pack(side="top",ipadx=10,ipady=10, fill="both",expand=True)

rectangle_3 = tk.Label(root, text="Rect3", bg="black", fg="white")
rectangle_3.pack(side="left",ipadx=10,ipady=10, fill="both")

root.mainloop()
