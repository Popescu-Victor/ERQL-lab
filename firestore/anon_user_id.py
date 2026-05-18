import numpy as np
import random
import pandas as pd
import dotenv
import os


folder_path = dotenv.load_dotenv()
folder_path = os.getenv("FOLDER")

user_list = []


for file in folder_path:
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        user_list.append(df.iloc[:, 0].tolist())

print(user_list)
