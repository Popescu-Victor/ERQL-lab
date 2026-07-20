import pandas as pd
import pickle



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
        filename = input("Enter filename to save the dataframe (with .pkl extension): ")
        with open(filename, 'wb') as f:
            pickle.dump(dataframe, f)

    if user_input.lower() == "load":
        filename = input("Enter filename to load the dataframe (with .pkl extension): ")
        try:
            with open(filename, 'rb') as f:
                dataframe = pickle.load(f)
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