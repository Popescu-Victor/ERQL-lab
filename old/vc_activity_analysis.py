import pandas as pd
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext

root = tk.Tk()
root.title("'Non Comissioned' Organizational Tools")
root.geometry("400x300")

text_box = scrolledtext.ScrolledText(root,width=1000,height=40,highlightthickness=2, highlightbackground="gray",wrap=tk.WORD)
text_box.pack(padx=10, pady=10)


def main (file):
  # The section "Timestamp" is removed because when a class took place is irrelevant to determining the performance of teachers. The section "Alte Mentiuni" (which translates to 'Other remarks') is also removed because they're only relevant on a case by case basis and feature strings instead of integers, which are irrelevant to the reports this software generates.

  df = pd.read_csv(file)
  df = df.drop(columns=["Timestamp","Alte mentiuni"])
  df = df.dropna()
  df = df.replace("Nu", 0)
  df = df.replace("Da", 2)
  df = df.replace("Partial", 1)


  def row2list ():
    rows_as_lists = df.values.tolist()
    ratio = [1, 0.5, 1, 0.5, 2, 2, 1, 0.5, 1, 0.5] # As I've exmplained in the 'Tkinter - GUI' file, these ratios are based on the original guidelines for teacher performance during online classes. Certain criteria are worth more than others towards the toal score.
    print(len(ratio))
    return rows_as_lists, ratio

  def total_score ():
    rows_as_lists, ratio = row2list()
    for i in rows_as_lists:
      combined = zip(ratio, i[1:]) # And this is where the ratio variable is used to modify how much certain criteria count towards the final score.
      combined = [x * y for (x, y) in combined]
      
      texted = (str(i[0]) + " TOTAL = " + str(sum(combined)))
      print(texted)
      
      text_box.insert(tk.END, texted + "\n")



  return total_score()



def browse_file():
    from tkinter import filedialog
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    if file_path:
        print(main(file_path))



browse = tk.Button(root, text="Browse File", command=browse_file)
browse.pack(pady=10)


root.mainloop()
