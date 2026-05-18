import numpy as np
import random
import pandas as pd
import openpyxl
from dotenv import load_dotenv
import os


load_dotenv()
folder_path = os.getenv("FOLDER")

user_list = []

def username_to_anon_id(username):
    anon_id = (str(username)[:2] + str(username)[-2:] + str(len(username))).upper()
    return anon_id


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

id_dict = {}

print("Unique Anonymous User IDs:")
for user_id in user_list:
    new_id = username_to_anon_id(user_id)
    first_last_name = user_id.split(", ")
    if len(first_last_name) == 2:
        # print(first_last_name[1] + " " + first_last_name[0] + "  -->  " + str(new_id))
        id_dict[user_id] = new_id
    else:
        # print(user_id + "  -->  " + str(new_id))
        id_dict[user_id] = new_id

print(id_dict)
# db.collection("ANON_ID").document("QoC1bZaqHZk13gQnhUF8 ").set(id_dict, merge=True)