# Python AI & Data Analysis Learning Journey

This repository is a structured day-wise journal of my learning path in Python, Data Analysis, and Machine Learning foundations. Each day builds upon real-world developer practices using Python, NumPy, and Pandas. The focus is to gain not just syntax knowledge but also practical understanding useful for future AI and ML work.

---

## 📖 Index

- [Day 1: Python Basics](#day-1-python-basics)
- [Day 2: NumPy & Pandas Introduction](#day-2-numpy--pandas-introduction)
- [Day 3: Real-World Student Data Analysis](#day-3-real-world-student-data-analysis)
- [Day 4: Missing Data Handling & Data Cleaning](#day-4-missing-data-handling--data-cleaning)
- [What's Next?](#whats-next)
- [Project Structure](#project-structure)
- [About Me](#about-me)
- [License](#license)

---

## Day 1: Python Basics

### ✅ Topics Covered
- Variables, user input
- Defining and using functions
- Conditional statements (if/else)
- Loops, even/odd logic
- Lists (`append()`) and dictionaries

### 🔍 Why This Matters
Understanding Python fundamentals is the core of any software or data-related role. This day built the foundation for all logic and syntax that I use in future tasks.

### 🧪 Practice Highlights
- Wrote custom functions like `square(x)` and `evenOrOdd(num)`
- Took input using `input()` and applied logic
- Stored data using lists and dictionaries
- Iterated using `for` loop and used conditionals inside loop

---

## Day 2: NumPy & Pandas Introduction

### ✅ Topics Covered
- Creating NumPy arrays
- Array operations: `sum`, `mean`, `sqrt`, `min`, `max`
- Creating a Pandas DataFrame from dictionary
- Column access and filtering (`df['marks'] > 80`)

### 🔍 Why This Matters
NumPy and Pandas are two of the most-used libraries in data science and ML. Learning how to create and manipulate structured data is crucial for preprocessing and analysis.

### 🧪 Practice Highlights
- Created arrays of numbers and calculated statistics
- Created student DataFrame with `name`, `age`, and `marks`
- Filtered students with more than 80 marks
- Used `df['column'].mean()` for aggregation

---

## Day 3: Real-World Student Data Analysis

### ✅ Topics Covered
- Creating a real DataFrame for student marks
- Calculating `total` and `average` across multiple subjects
- Conditional grading (A, B, C, etc.)
- Filtering students based on performance
- Displaying selected columns for reporting

### 🔍 Why This Matters
Before diving into ML, it’s important to simulate real data use-cases. This day focused on turning raw marks into actionable results — a core data analyst task.

### 🧪 Practice Highlights
- Used `.sum(axis=1)` for row-wise total
- Applied multiple filters using logical operators (`&`)
- Used conditional logic to assign grades
- Filtered students who scored >85 in all subjects

---

## Day 4: Missing Data Handling & Data Cleaning

### ✅ Topics Covered
- Introduced `NaN` values in dataset
- Used `isnull()`, `isnull().sum()` to detect missing values
- Used `fillna()` with column-wise `mean()` to fill missing data
- Used loop to apply cleaning dynamically for all columns

### 📌 Why This Is Important
In real-world data, missing values are extremely common (in surveys, forms, scraped data). Models break if data isn’t cleaned properly. That’s why this is a critical preprocessing step in ML pipelines.

### 🔍 What is a Missing Value in Pandas?
- A missing value can be `NaN`, `None`, or a blank cell.
- `NaN` stands for “Not a Number” and is handled using Pandas functions.

### 🧪 Practice Highlights
- Used `df.fillna(df.mean(), inplace=True)` for quick fix
- Used column-wise approach: `df['col'] = df['col'].fillna(df['col'].mean())`
- Used loop to apply mean-filling on all numeric columns
- Cleaned and re-used the DataFrame for further filtering

---

## Day 5 - Data Visualization

### 1. Bar Plot (Vertical Bar Chart)

A bar plot or bar chart is a graph that represents **categories of data** with rectangular bars. The **height of each bar** corresponds to the value it represents. It is used to compare things between different groups or to track changes over time (when the time is discrete).

We use the `bar()` method from `matplotlib.pyplot` to create a vertical bar chart.

---

#### 🖼 Output:
![Bar Chart](day5-Practice/output_bar_chart.png)

---

## About Me

**Karan Bharvadiya**  
Final Year CSE Student | GEC Rajkot  
Actively learning Python, Data Science, and AI fundamentals.  
Also experienced with Laravel (PHP), Tailwind CSS, and Web Development.

GitHub: [https://github.com/your-username](https://github.com/your-username)

---

## License

This repository is part of my personal learning journey.  
You may use the structure or content for self-learning or reference.  
No commercial redistribution allowed.


