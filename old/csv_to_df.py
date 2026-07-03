# Used when I was learning how to use pandas dataframes
import pandas as pd 



input = "Delia --> 112300022"
clean = input.split(' --> ')
result = [clean[0]] + list(clean[1])
print(result)


df = pd.read_csv(r'test.csv')
new_row = pd.DataFrame([result], columns=df.columns)
df = pd.concat([df, new_row], ignore_index=True)
df.to_csv(r'test.csv', index=False)
