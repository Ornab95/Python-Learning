import pandas as pd
import matplotlib.pyplot as plt

# x = [1, 2, 3, 4,5]
# y = [10, 20, 15, 30,35]
# plt.plot(x, y)
# plt.title('Simple Line Plot')
# plt.xlabel('X-axis -> time')
# plt.ylabel('Y-axis -> values')

# # plt.show()

df = pd.read_csv('Python Library/Store.csv')
# print(df)

# plt.hist2d(df["Cost"], df["Profit"], bins=[30, 30], cmap='Blues')
# plt.title('Cost vs Profit')
# plt.xlabel('Cost')
# plt.ylabel('Profit')
# plt.colorbar(label='Counts')
# plt.show()

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [2500, 2700, 3000, 2800, 3200, 3500, 4000, 4200, 4500, 4800, 5000, 5500]
Buying = [1500, 1700, 2000, 1800, 2200, 2500, 3000, 3200, 3500, 3800, 4000, 4500]

plt.plot(month, sales, color='skyblue',linestyle='--', marker='o')
plt.plot(month, Buying, color='black', linestyle=':', marker='x')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales amount in dollars ($)')
plt.legend(['Sales', 'Buying'])
plt.grid(color = 'gray', linestyle = '--', linewidth = 1)
plt.show()