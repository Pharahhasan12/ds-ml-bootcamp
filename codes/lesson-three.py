import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'dataset/care pricev_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

df["Size_sqft"] = df["Size_sqft"].fillna(df["Size_sqft"].median())
df["Bedrooms"] = df["Bedrooms"].fillna(df["Bedrooms"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
