import numpy as np
import pandas as pd


def test_clean():
    # Load the data
    df = pd.read_csv('PS_2024.05.16_14.06.35.csv')
    # Drop rows with missing values
    # df = df.dropna()
    # Display stats
    print(df.describe())


test_clean()