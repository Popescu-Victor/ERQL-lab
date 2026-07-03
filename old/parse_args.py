import pandas as pd
import pickle
from charset_normalizer import from_path


print("Welcome to the ERQL CLI. Type 'exit' to quit.")


def main(args):

    if len(args) == 0:
        print("No arguments provided. Please provide a command.")
        return
    if args[0] == "file": # Commands related to files on the device.
        if args[1] == "select":
            from src.args_file import Filepath
            from tkinter import filedialog
            filepath = filedialog.askopenfilename(title="Select a file", filetypes=[("CSV files", "*.csv")])
            if filepath:
                print(f"Selected file: {filepath}")
                global selected_file
                selected_file = Filepath(filepath)
                result = from_path(selected_file.path).best()
                global dataframe
                dataframe = pd.read_csv(selected_file.path, encoding=result.encoding)
                return selected_file, dataframe
            else:
                print("No file selected.")
                return None

        if args[1] == "path":
            if selected_file is not None:
                print(f"Current file path: {selected_file}")
            else:
                print("No file path set.")

        if args[1] == "info":
            print(f"File info:\n{dataframe.info()}")

        if args[1] == "head":
            print(f"File head:\n{dataframe.head()}")

        if args[1] == "details":
            print(f"File details:\n{dataframe.describe()}")



    if args[0] == "dataframe": # Create and edit a blank dataframe.
        if args[1] == "new":
            from src import dataframes
            col_list = input("Write the names of the columns separated by comma >>  ").split(',')
            global df
            df = dataframes.CLI_Dataframe(col_list)

        if args[1] == "add":
            user_input = input(">>")
            while user_input != "done":
                df.add_row(input(">>").split(','))
        if args[1] == "cols":
            print(df.head())

    if args[0] == "ask": # API request to Gemini Flash.
        from src import ask_gemini_flash
        ask_gemini_flash.main(args[1:])
    
    if args[0] == "convert": # Convert scraped ILIAS content into readable format.
        from src import ilias_convert
        ilias_convert.convert_csv_to_ilias_format(args[1:])