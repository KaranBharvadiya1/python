import matplotlib.pyplot as plt

subjects = ['Maths', 'Science', 'English', 'History']
marks = [90, 85, 88, 92]

plt.bar(subjects, marks, color = 'skyblue')

plt.title("Subjects-wise Marks")
plt.xlabel("subjects", color = 'red')
plt.ylabel("Marks", color = 'red')

plt.ylim(0, 100)

plt.show()