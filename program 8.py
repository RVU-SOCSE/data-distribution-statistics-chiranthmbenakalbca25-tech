import pandas as pd
# Load the CSV file
df = pd.read_csv('C:/Users/RVUW233/Desktop/chiru/python/prog7.csv')

# Displaying the basic central tendencies and dispersion metrics
mean_value = df['Year'].mean()
median_value = df['Year'].median()
mode_value = df['Year'].mode()[0] # In case of multiple modes, we take the first one
min_value = df['Year'].min()
max_value = df['Year'].max()
variance_value = df['Year'].var()
std_dev_value = df['Year'].std()

# Printing the results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value}")
