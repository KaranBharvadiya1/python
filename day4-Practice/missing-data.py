import pandas as pd
import numpy as np

data = {
    "name": ["Karan", "Pravin", "Nita", "Manisha"],
    "Maths": [90, 83, np.nan, 91],
    "Science": [85, 88, 90, np.nan],
    "English": [88, 90, 85, 89],
    "History": [92, 85, 88, 90],
    "Geography": [89, 87, 90, 91],
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Fill missing values with column-wise mean
df.fillna(df.mean(numeric_only=True), inplace=True)

print("\nDataFrame after filling missing values with mean:")
print(df)
