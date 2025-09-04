import pandas as pd
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'Age': [25, 30, 35, 28, 32],
#     # "EmpId": [101, None, 103, 104, 105],
#     'Salary': [70000, 80000, 90000, 75000, 82000],
#     'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Seattle'],
#     'Performance': [85, 90, 95, 88, 92]
# }
# df = pd.DataFrame(data)
# # print("Original DataFrame:")
# # print(df)

# # Add a new column 'Experience' based on 'Age'
# df["Experience"] = df["Age"] - 24
# print("\nDataFrame after adding 'Experience' column:")
# # print(df)
# # using insert method
# df.insert(0, "Employee ID", [1, 2, 3, 4, 5])
# print(df)

# #Updating Values
# df.loc[0, "Salary"] = 72000
# print(df)

# #Updating value (Increasing all value by 10% )
# df["Salary"] = df["Salary"] * 1.1
# print("\nDataFrame after increasing 'Salary' by 10  %:")
# print(df)

# # Drop a Single Column
# df.drop("Experience", axis=1, inplace=True)
# print("\nDataFrame after dropping 'Experience' column:")
# print(df)

# # Drop Multiple Columns
# df.drop(["City", "Performance"], axis=1, inplace=True)
# print("\nDataFrame after dropping 'City' and 'Performance' columns:")
# print(df)

#NaN Values
# print(df.isnull().sum()) 


df2 = pd.read_csv("Titanic-Dataset.csv")
print(df2.isnull().sum())
print(df2["Age"].head())
print(df2["Age"].mean())

# Drop NA
# df2.dropna(axis=1, inplace=True)
# print("\nDataFrame after dropping columns with NA values:")
# print(df2.isnull().sum())

# Fill NA
# df2["Age"].fillna(df2["Age"].mean(), inplace=True)
# print("\nDataFrame after filling NA values with column means:")
# print(df2.isnull().sum()) 

# print(df2["Age"].mean())

# Interpolate Method
df2["Age"].interpolate(method="linear",axis=1 ,inplace=True) # Linear 2 Polynomial
print("\nDataFrame after interpolating NA values:")
print(df2.isnull().sum())
print(df2["Age"].head())

  