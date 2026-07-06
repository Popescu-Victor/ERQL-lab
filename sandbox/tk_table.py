import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack()

canvas.create_text(
    20, 20,
    text="Hello, world!",
    anchor="nw",
    font=("Arial", 14)
)

canvas.create_text(
    20, 60,
    text="This is a longer line of text.",
    anchor="nw",
    fill="blue"
)

root.mainloop()