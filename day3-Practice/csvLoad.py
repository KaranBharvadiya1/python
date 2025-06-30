import pandas as pd
import numpy as np

data = {
    "name": ["Karan", "Pravin", "Nita", "Manisha"],
    "Maths": [90, 83, 87, 91],
    "Science": [85, 88, 90, 92],
    "English": [88, 90, 85, 89],
    "History": [92, 85, 88, 90],
    "Geography": [89, 87, 90, 91],
}

df = pd.DataFrame(data)

# Total & Average
df['total'] = df[['Maths', 'Science', 'English', 'History', 'Geography']].sum(axis=1)
df['average'] = df['total'] / 5

# Top Students
top_students = df[df["average"] > 89]
print("\nTop Students:")
print(top_students[['name', 'average']])

# Assign Grades
conditions = [
    (df['average'] >= 90),
    (df['average'] >= 80),
    (df['average'] >= 60),
    (df['average'] >= 40),
]
grades = ['A', 'B', 'C', 'D']
df['grade'] = np.select(conditions, grades, default='F')

# Final Output
print("\nStudents with Grades:")
print(df[['name', 'average', 'grade']])
