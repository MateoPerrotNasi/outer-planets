import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data/all_exoplanets_2021.csv')

# Drop the rows with missing values
data = data.dropna()

print(data.head())
print(data.describe())
