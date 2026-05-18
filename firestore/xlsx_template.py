import numpy as np
import random
import pandas as pd
import openpyxl
from dotenv import load_dotenv
import os


load_dotenv()
folder_path = os.getenv("FOLDER")

if not folder_path:
    raise ValueError("FOLDER is not set in your .env file")

data_dict = {}

for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        filepath = os.path.join(folder_path, filename)
        print(f"Processing file: {filepath}")
        
        wb = openpyxl.load_workbook(filepath)
        ws = wb.active
        
        for row in ws.iter_rows(values_only=True):
            if row[1] is not None:
                key = row[1]
                data_dict[key] = data_dict.get(key, 0) + 1

print(data_dict)