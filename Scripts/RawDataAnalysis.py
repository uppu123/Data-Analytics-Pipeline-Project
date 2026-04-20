import pandas as pd
import numpy as np
import os

# Path to your data folder
DATA_PATH = "../1_Data/raw/"

files = [
    "attendance.csv",
    "events.csv",
    "registrations.csv",
    "sponsors.csv"
]

def analyze_dataset(file_path):
    print(f"\n{'='*60}")
    print(f"Analyzing: {file_path}")
    print(f"{'='*60}")
    
    df = pd.read_csv(file_path)
    
    # Basic Info
    print("Shape:", df.shape)
    print("Data Types:\n", df.dtypes)
    
    # Missing / Null Values
    print("Missing Values (Column-wise):")
    print(df.isnull().sum())
    
    print("Total Missing Values:", df.isnull().sum().sum())
    
    # Duplicate Rows
    print("Duplicate Rows:", df.duplicated().sum())
    
    # Unique Values
    print("Unique Values per Column:")
    print(df.nunique())
    
    # Basic Statistics
    print("Statistical Summary:")
    print(df.describe(include='all'))
    
    # Outlier Detection using IQR
    print("Outliers (Numerical Columns using IQR):")
    numeric_cols = df.select_dtypes(include=np.number).columns
    
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        
        print(f"{col}: {len(outliers)} outliers")
    
    print("\n Analysis Complete")

# Run analysis on all files
for file in files:
    file_path = os.path.join(DATA_PATH, file)
    analyze_dataset(file_path)