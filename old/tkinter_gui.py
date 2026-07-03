import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("'Non Comissioned' Organizational Tools")
root.resizable(False, False)

choice = tk.StringVar(root)
choice.set("Virtual Classroom Analyser") 

tools = ["Virtual Classroom Analyser", "Scraper → SCORM Code"]

dropdown = tk.OptionMenu(root, choice, *tools)
dropdown.pack(padx=20, pady=20)


def browse_file():
    from tkinter import filedialog
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    if file_path:
        print("Selected file:", file_path)

canvas_default = tk.Canvas(root, width=400, height=300, bg="gray70", highlightthickness=2, highlightbackground="gray")
canvas_default.place(x=50, y=50)
canvas_default.pack(padx=10, pady=10)
    
browse = tk.Button(root, text="Browse File", command=browse_file)
browse.pack(pady=10)

def provide_tool():
    btn.pack_forget()
    browse.pack_forget()
    canvas_default.pack_forget()
    if choice.get() == "Virtual Classroom Analyser":

        canvas = tk.Canvas(root, width=400, height=300, bg="white", highlightthickness=2, highlightbackground="gray")
        canvas.place(x=50, y=50)
        canvas.pack(padx=10, pady=10)

    if choice.get() == "Scraper → SCORM Code":

        text_box = scrolledtext.ScrolledText(root,width=50,height=15,highlightthickness=2, highlightbackground="gray",wrap=tk.WORD)
        text_box.pack(padx=10, pady=10)

btn = tk.Button(root, text="Return", command=provide_tool)
btn.pack()


root.mainloop()
