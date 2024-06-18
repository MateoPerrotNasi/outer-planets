import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data/all_exoplanets_2021.csv')
print(data.shape[0])

# Drop the rows with missing values
# drop rows that have any of the following columns missing: Planet Name, Host Name, Orbital Period [days], Orbit Semi-Major Axis [au], Stellar Effective Temperature [K], Equilibrium Temperature [K], Insolation Flux [Earth Flux]

columns_to_check = [
    'Planet Name', 'Planet Host', 'Orbital Period Days',
    'Orbit Semi-Major Axis', 'Stellar Effective Temperature',
    'Equilibrium Temperature', 'Insolation Flux'
]

# Drop rows with missing values in the specified columns
df_cleaned = data.dropna(subset=columns_to_check)

# Get the number of rows after removing NAs
num_rows_cleaned = df_cleaned.shape[0]

print("Number of rows after removing specified columns with NAs:", num_rows_cleaned)
