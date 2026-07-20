import pandas as pd
import pickle



def new_df():
    col_no = input("How many columns do you want in your new dataframe? >> ")
    col_names = []
    for i in range(int(col_no)):
        col_name = input(f"Enter name for column {i+1}: ")
        col_names.append(col_name)
    return pd.DataFrame(columns=col_names)

dataframe = new_df()

while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        print("Exiting the program.")
        break
    if user_input.lower() == "print":
        print(dataframe)
    else:
        new_row = []
        for col in dataframe.columns:
            value = input(f"Enter value for column '{col}': ")
            new_row.append(value)
        dataframe.loc[len(dataframe)] = new_row
        print("Row added successfully.")
        print(dataframe)