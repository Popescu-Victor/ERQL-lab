import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# What I'm trying to do here is create a button that would toggle the display of a trendline in the data. Right now, it mostly makes sense for scatterplots, not other types of graphs.

root = tk.Tk()
hor = []
vert = []

def browse_file():
    from tkinter import filedialog
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
    
    if file_path:
        df = pd.read_csv(file_path)
        coeffs = np.polyfit(hor, vert, 1)
        trendline = np.poly1d(coeffs)

plt.scatter(hor, vert ,color='red', s=100, alpha=0.3)

plt.xlabel(hor.name)
plt.ylabel(vert.name)
plt.plot(hor, trendline(hor),linestyle="--", color='indianred', label="Trendline")

print("The Correlation is: " + str(vert.corr(hor)))

show = True
if show == True:
    dfk = pd.read_csv('bcak.csv')
    hork = dfk[hor.name]
    vertk = dfk[vert.name]
    trendlinek = np.poly1d(np.polyfit(hork, vertk, 1))
    plt.scatter(hork, vertk ,color='blue', s=30, alpha=0.2)
    plt.plot(hork, trendlinek(hork),linestyle=":", color='lightblue', label="Trendline")
    print("The Correlation in K is: " + str(vertk.corr(hork)))


plt.xlim()
plt.ylim()
plt.show()




browse_cv = tk.Button(root, text="browse", command=browse_file)
browse_cv.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)



root.mainloop()
