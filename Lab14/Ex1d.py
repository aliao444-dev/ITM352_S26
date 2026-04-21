# Exercise 1d - Line + scatter of x1/y1, plus second line graph of x2/y2

import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 4, 7]

plt.plot(x1, y1)
plt.scatter(x1, y1)
plt.plot(x2, y2)
plt.show()
