import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load the data
data = pd.read_csv('data/all_exoplanets_2021.csv')
print("Initial number of rows:", data.shape[0])

# Define the columns to check for missing values
columns_to_check = [
    'Planet Name', 'Planet Host', 'Orbital Period Days',
    'Orbit Semi-Major Axis', 'Stellar Effective Temperature',
    'Equilibrium Temperature', 'Insolation Flux'
]

# Drop rows with missing values in the specified columns
df_cleaned = data.dropna(subset=columns_to_check)
print("Number of rows after removing specified columns with NAs:", df_cleaned.shape[0])


# Define the Goldilock zone boundaries based on stellar effective temperature
def calculate_goldilock_boundaries(stellar_temp):
    inner_boundary = 0.95 * np.sqrt(stellar_temp / 5780)  # Adjusted boundaries for more accuracy
    outer_boundary = 1.37 * np.sqrt(stellar_temp / 5780)  # Adjusted boundaries for more accuracy
    return inner_boundary, outer_boundary


# Create a function to determine if a planet is in the Goldilock zone
def is_in_goldilock_zone(row):
    inner_boundary, outer_boundary = calculate_goldilock_boundaries(row['Stellar Effective Temperature'])
    return 1 if inner_boundary <= row['Orbit Semi-Major Axis'] <= outer_boundary else 0


# Apply the function to create a new column 'Is In Goldilock'
df_cleaned['Is In Goldilock'] = df_cleaned.apply(is_in_goldilock_zone, axis=1)

# Print the first few rows to verify the new column
print(df_cleaned[['Planet Name', 'Planet Host', 'Orbit Semi-Major Axis', 'Stellar Effective Temperature',
                  'Is In Goldilock']].head())

# Select features and target variable
features = ['Orbit Semi-Major Axis', 'Stellar Effective Temperature', 'Insolation Flux']
X = df_cleaned[features]
y = df_cleaned['Is In Goldilock']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Plot feature importances
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure()
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices], color="r", align="center")
plt.xticks(range(X.shape[1]), [features[i] for i in indices], rotation=90)
plt.xlim([-1, X.shape[1]])
plt.show()
