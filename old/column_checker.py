class ColumnChecker:
    def __init__(self, df):
        self.df = df
        self.indicator = 'Test Passes'

    def check_column(self, column_no):
        col = self.df.iloc[:, int(column_no)]

        if any(self.indicator in i for i in col):
            for i in col:
                print(i.replace('Test Passes for Participant: ', ''))
        else:
            print('Error: Wrong Column Index')
