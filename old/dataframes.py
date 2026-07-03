import pandas as pd
# Creating a pandas dataframe from scrath.

class CLI_Dataframe():
    def __init__(self, columns):
        self.df = pd.DataFrame(columns=columns)

    def add_row(self, row):
        self.df.loc[len(self.df)] = row

    def head(self):
        df_head = self.df.head()
        return df_head
