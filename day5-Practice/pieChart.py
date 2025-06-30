import matplotlib.pyplot as plt

activities = ['Study', 'Exercise', 'Sleep', 'Entertainment']
time_spent = [5, 1, 7, 3]

plt.pie(time_spent, labels=activities, autopct='%1.1f%%', startangle=140)
plt.title("Daily Time Distribution")
plt.show()
