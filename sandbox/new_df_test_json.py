import pandas as pd
import json

# JSON might be better than Pickle for saving and loading dataframes because JSON is a widely used format that is human-readable and can be easily shared across different programming languages. Pickle, on the other hand, is Python-specific and may not be compatible with other languages or versions of Python. Additionally, JSON files can be easily edited and viewed in text editors, while Pickle files are binary and not easily readable.

def new_df():
    col_no = input("How many columns do you want in your new dataframe? >> ")
    col_names = []
    for i in range(int(col_no)):
        col_name = input(f"Enter name for column {i+1}: ")
        col_names.append(col_name)
    return pd.DataFrame(columns=col_names)


while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        print("Exiting the program.")
        break

    if user_input.lower() == "new":
        dataframe = new_df()

    if user_input.lower() == "print":
        print(dataframe)

    if user_input.lower() == "save":
        filename = input("Enter filename to save the dataframe (with .json extension): ")
        dataframe.to_json(filename, orient="records")

    if user_input.lower() == "load":
        filename = input("Enter filename to load the dataframe (with .json extension): ")
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                dataframe = pd.DataFrame(data)
        except FileNotFoundError:
            print(f"File '{filename}' not found. Please check the filename and try again.")
            
    else:
        new_row = []
        for col in dataframe.columns:
            value = input(f"Enter value for column '{col}': ")
            new_row.append(value)
        dataframe.loc[len(dataframe)] = new_row
        print("Row added successfully.")
        print(dataframe)