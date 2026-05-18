import numpy as np
import random
import pandas as pd
import openpyxl
from dotenv import load_dotenv
import os


load_dotenv()
folder_path = os.getenv("FOLDER")

for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx") and not filename.startswith("~$"): # and not filename.startswith("~$") - This part skips temp files in folder created by opening excel files
        filepath = os.path.join(folder_path, filename)
        
        wb = openpyxl.load_workbook(filepath)
        ws = wb.active
                
        for row in ws.iter_rows(values_only=True):
            for col_index, cell in enumerate(row):
                if cell == "Test Passes for Participant: ":
                    print(f"Found in column index {col_index}")
                    break
