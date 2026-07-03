import tkinter as tk
import pandas as pd
from tkinter import scrolledtext
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict
import sqlite3

database = sqlite3.connect('database.db')
curs = database.cursor()

curs.execute(''' CREATE TABLE hw_clean (username, links) ''')

# This section is for creating the GUI with Tkinter 

root = tk.Tk()
root.title("'Non Comissioned' Organizational Tools")
root.geometry("800x600")

# The layout is as follows: four sections, the two on top being much taller and meant for displays the the two on the bottom for the buttons.
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)

text_box = scrolledtext.ScrolledText(root,width=30,height=20,highlightthickness=2, highlightbackground="gray",wrap=tk.WORD)
text_box.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

canvas1 = tk.Frame(root)
canvas1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# This function cleans data from the reports related to teacher performance during online classes and then return the average performance over the course of a semester both as text and as a bar chart.
def browse_analiza():
    
    from tkinter import filedialog
    file = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    #This part is for cleaning the data up before I do anything with it.
    df = pd.read_csv(file)
    df = df.drop(columns=["Timestamp","Alte mentiuni"])
    df = df.dropna()
    df = df.replace("Nu", 0)
    df = df.replace("Da", 2)
    df = df.replace("Partial", 1)

    # And this is for returning the final score for the teacher's performance as text.
    scor_deprinderi = [1, 0.5, 1, 0.5, 2, 2, 1, 0.5, 1, 0.5]
    df["Total"] = df.iloc[:, 1:11].mul(scor_deprinderi).sum(axis=1)
    avg_table = (df.groupby(df.columns[0], as_index=False)["Total"].mean())
    avg_table["Total"] = avg_table["Total"] * 5
    for _, row in avg_table.iterrows():
        text_box.insert(tk.END, f"{row['Nume Tutore']}: {round(row['Total'])}%\n")

    # This is for returning the final score as bar chart.
    avg_table = avg_table.sort_values("Total", ascending=True)
    fig = Figure(figsize=(6, 4))
    ax = fig.add_subplot(111)
    ax.barh(avg_table["Nume Tutore"], avg_table["Total"])
    ax.set_xlabel("Total")

    chart = FigureCanvasTkAgg(fig, master=canvas1)
    chart.draw()
    chart.get_tk_widget().pack(fill="both", expand=True)

# This function cleans data related to student's non graded homework and returns two things: a pie chart to beter visualize which of the teachers is falling behind on grading homework and a text that can be pasted into ILIAS that returns links to these grading tasks.
def browse_hw():
    from tkinter import filedialog
    file = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    
    df = pd.read_csv(file)
    hw_link = df.iloc[:, 4].tolist()
    student_username = df.iloc[:, 6].tolist()
    counts = df.iloc[:, 6].value_counts()

# This section might be a bit confusing for someone that has never used the ILIAS LMS. This does two things: First, it removes the part that automatically comes with the scraped username section in homework areas 'Test Passes for Participant' (The word "test" here refers to both tests and regular homework). Secondly, it provides teachers a link to the assignments that are still to be graded instead of just telling them which exercises those are.

    student_username = [i.replace("Test Passes for Participant: ", "") for i in student_username]
    hw_link = [i.replace(i, '''[xln url="'''+ i + '''"]Link[/xln]''') for i in hw_link] # The temp variable 'i' here is the link to the ungraded assignment.
    curs.commit()
    
    result = defaultdict(list)

    for k, v in zip(student_username, hw_link):
        result[k].append(v)

    output_final = ["Nume\tNumar Teme Necorectate\tLinkuri"]
    for k, v in result.items():
        output_final.append(f"{k} are {len(v)} teme necorectate: {' '.join(v)} ")

    text_box.insert(tk.END, "\n".join(output_final))
    
    fig, ax = plt.subplots()
    labels_rem = [label.replace("Test Passes for Participant:", "") for label in counts.index]
    ax.pie(counts.values, labels=labels_rem, autopct='%1.1f%%')
    ax.set_title("Procentant Cursant din Total")
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0)

# There's two things this small app is used for: creating homework reports and reating live class reports. These two buttons are for separating the two tasks.
btn1 = tk.Button(root, text="Formatare Teme", command=browse_hw)
btn1.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

btn2 = tk.Button(root, text="Analiza Clase Virtuale", command=browse_analiza)
btn2.grid(row=1, column=1, sticky="ew", padx=10, pady=10)


root.mainloop()
