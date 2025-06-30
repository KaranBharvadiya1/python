import matplotlib.pyplot as plt

subjects = ['Maths', 'Science', 'English', 'History']
karan_marks = [90, 85, 88, 92]
pravin_marks = [83, 88, 90, 85]

plt.plot(subjects, karan_marks, marker='o', label='Karan', color='blue')
plt.plot(subjects, pravin_marks, marker='s', label='Pravin', color='orange')

plt.title("Subjects-wise Marks Comparison")
plt.xlabel("Subjects", color='red')
plt.ylabel("Marks", color='red')

plt.ylim(0, 100)
plt.legend()
plt.grid(True)
plt.show()