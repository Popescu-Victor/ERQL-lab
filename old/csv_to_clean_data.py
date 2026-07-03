import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import gradio as gr # This library is for creating an interface that doesn't require opening .exe files, which is important since I and the other teachers using this are running the code off of military computers.

def file_return(file): # The issue with this part is that it requires data to always be in the same column, which is not the case.
    
    if isinstance(file, str):  # Gradio library update on February 27th requires this part.
        filepath = file
    elif hasattr(file, "name"):
        filepath = file.name
    else:
        filepath = file["name"]


    df = pd.read_csv(file.name)
    hw_link = df.iloc[:, 5].tolist()
    student_username = df.iloc[:, 7].tolist()
    
    student_username = [i.replace("Test Passes for Participant: ", "") for i in student_username]
    hw_link = [i.replace(i, '''[xln url="'''+ i + '''"]Link[/xln]''') for i in hw_link]
    
    result = defaultdict(list)

    for k, v in zip(student_username, hw_link):
        result[k].append(v)

    output_final = ["Nume\tNumar Teme Necorectate\tLinkuri"]
    for k, v in result.items():
        output_final.append(f"{k} are {len(v)} teme necorectate: {' '.join(v)} ")
    return "\n".join(output_final)

    # Insert grid layout and plot data.
    fig, ax = plt.subplots()
    labels_rem = [label.replace("Test Passes for Participant:", "") for label in counts.index]
    ax.pie(counts.values, labels=labels_rem, autopct='%1.1f%%')
    ax.set_title("Procentant Cursant din Total")

iface = gr.Interface(
    fn=file_return,
    inputs=gr.File(file_types=[".csv"]),
    outputs=gr.Textbox(lines=50)
)

iface.launch()
