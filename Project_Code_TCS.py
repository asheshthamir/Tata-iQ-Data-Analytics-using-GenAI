import pandas as pd

# Load the dataset
df = pd.read_csv('Delinquency_prediction_dataset.csv')

# 1. Check for missing values
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]

# 2. Check for anomalies (Description of data)
description = df.describe()

# 3. Check for duplicates
duplicates = df.duplicated().sum()

# 4. Check Risk Indicators (Correlation with Delinquency)
# Assuming 'Delinquent' is the target column (0 or 1)
# Converting to numeric if needed to check correlation
numeric_df = df.select_dtypes(include=['number'])
correlation = numeric_df.corr()['Delinquent'].sort_values(ascending=False)

# Display findings
print("Missing Values:\n", missing_values)
print("\nDescription:\n", description)
print("\nDuplicates:", duplicates)
print("\nCorrelation with Delinquency:\n", correlation)