import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

rectangle_1 = tk.Label(main, text="Label top", bg="red", fg="white")
rectangle_1.pack(side="top",ipadx=10, ipady=10,fill="both",expand=True)

rectangle_2 = tk.Label(main, text="Label top", bg="red", fg="white")
rectangle_2.pack(side="top",ipadx=10,ipady=10, fill="both",expand=True)

rectangle_3 = tk.Label(root, text="Label left", bg="green", fg="white")
rectangle_3.pack(side="left",ipadx=10,ipady=10, fill="both", expand=True)

root.mainloop()
