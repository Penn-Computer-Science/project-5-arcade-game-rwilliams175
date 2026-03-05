import tkinter as tk
import random

root = tk.Tk()
root.title("Colosseum Waves")
root.geometry("1920x1080")
canvas = tk.Canvas(root, width=960, height = 540)
canvas.pack()

player = canvas.create_rectangle()


root.mainloop()