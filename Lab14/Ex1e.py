# Exercise 1e - Full plot with title and axis labels

import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 4, 7]

plt.plot(x1, y1, label='Series 1 (line)')
plt.scatter(x1, y1, label='Series 1 (scatter)')
plt.plot(x2, y2, label='Series 2 (line)')

plt.title('Sample Line and Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()
plt.show()
