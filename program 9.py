import pandas as pd

# Load the CSV file
df = pd.read_csv('C:/Users/RVUW233/Desktop/chiru/python/prog7.csv')
# Statistical summary of the data using describe()
description = df.describe()
# Calculating quantiles
quantiles = df['Year'].quantile([0.25, 0.5, 0.75])
# Calculating skewness and kurtosis
skewness = df['Year'].skew()
kurtosis = df['Year'].kurt()
# Calculating value counts for unique values in the 'YearsExperience' column
value_counts = df['Year'].value_counts()
# Displaying the results
print("Statistical Summary:\n", description)
print("\nQuantiles:\n", quantiles)
print("\nSkewness:", skewness)
print("Kurtosis:", kurtosis)
print("\nValue Counts:\n", value_counts)
