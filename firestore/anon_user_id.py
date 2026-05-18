import numpy as np
import random
import pandas as pd
import openpyxl
from dotenv import load_dotenv
import os


load_dotenv()
folder_path = os.getenv("FOLDER")

user_list = []


for filename in os.listdir(folder_path):

    if filename.endswith(".xlsx") and not filename.startswith("~$"): # and not filename.startswith("~$") - This part skips temp files in folder created by opening excel files
        filepath = os.path.join(folder_path, filename)
        
        df = pd.read_excel(filepath)

        for col in df.columns:
            if df[col].astype(str).str.contains("Test Passes", na=False).any():
                column_index = df.columns.get_loc(col)
                for index, value in df[col].items():
                    if "Test Passes for Participant: " in str(value):
                        anon_user_id = value.split("Test Passes for Participant: ")[1]
                        if anon_user_id not in user_list:
                            user_list.append(anon_user_id)

print("Unique Anonymous User IDs:")
for user_id in user_list:
    print(user_id)