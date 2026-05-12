"""
Pandas: Handling Missing Data
Detecting and filling missing values in DataFrames
"""

import pandas as pd

# Load CSV file (assuming the archive folder exists)
try:
    df = pd.read_csv('./archive/apple.csv')
    
    print("=" * 50)
    print("Handling Missing Data")
    print("=" * 50)
    
    print("\nCheck for missing values:")
    print(df.isna())
    
    print("\nCount missing values per column:")
    print("df.isna().sum() =")
    print(df.isna().sum())
    
    print("\nFind rows with missing 'storage' column:")
    isna_check = df[df['storage'].isna()]
    print("Rows with NA in storage:", len(isna_check))
    
    print("\nDataFrame before filling NA:")
    print(df.tail())
    
    print("\nFill NA values with 0:")
    df = df.fillna(0)
    
    print("\nDataFrame after filling NA:")
    print(df.tail())
    
except FileNotFoundError:
    print("Note: CSV file not found. Create './archive/apple.csv' to run this script.")
