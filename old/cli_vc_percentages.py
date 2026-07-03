import pandas as pd

# The original Google Forms doc had the following options for each class entry objective: "Yes" (Fulfilled), "No" (Not fulfilled), "Partially". In order to convert the entries into usable data, I've converted these into integers and cleaned the data as shown below:

df = pd.read_csv("cv.csv")
df = df.drop(columns=["Timestamp","Alte mentiuni"])
df = df.dropna()
df = df.replace("Nu", 0)
df = df.replace("Da", 2)
df = df.replace("Partial", 1)

# As per the documentation, not every kind of entry is worth the same towards the overall score, which is why the part below converts the scores properly:

rows_as_lists = df.values.tolist()
ratio = [1, 0.5, 1, 0.5, 2, 2, 1, 0.5, 1, 0.5]
print(len(ratio))
combined = 0

for i in rows_as_lists:
  combined = zip(ratio, i[1:])
  combined = [x * y for (x, y) in combined]
  print(str(combined) + str(i[0]) + " total = " + str(sum(combined)))

# Listing out the final score for each entry:

for i in rows_as_lists:
  print(str(i[0]) + " are ca rezultate: " + str(i[1:]))
