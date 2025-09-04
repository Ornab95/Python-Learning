import pandas as pd
import matplotlib.pyplot as plt

x = [1, 2, 3, 4,5]
y = [10, 20, 15, 30,35]
plt.plot(x, y)
plt.title('Simple Line Plot')
plt.xlabel('X-axis -> time')
plt.ylabel('Y-axis -> values')

plt.show()