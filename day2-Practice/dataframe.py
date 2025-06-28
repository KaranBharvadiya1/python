import pandas as pd

data = {
    'name' : ['Karan', 'Pravin', 'Nita'],
    'age' : [21, 24, 25],
    'marks' : [90, 80, 85],
}

df = pd.DataFrame(data)

print(df)
print(type(df))

print("students with more than 80 marks:")
print(df[df['marks'] > 80]['name'])

print("Average Marks:", df['marks'].mean())
