"""
Pandas: Basic DataFrame Operations
Reading, viewing, and basic transformations on DataFrames
"""

import pandas as pd

# Load CSV file (assuming the archive folder exists)
try:
    df = pd.read_csv('./archive/apple.csv')
    
    print("=" * 50)
    print("Basic DataFrame Operations")
    print("=" * 50)
    
    print("\nFirst 5 rows:")
    print(df.head())
    
    print("\nLast 5 rows:")
    print(df.tail())
    
    print("\nBasic statistics:")
    print(df.describe())
    
    print("\nFilter specific columns:")
    print(df.filter(['year', 'month'], axis=1))
    
    print("\nRename columns:")
    print(df.rename(columns={'sale_id': 'id'}))
    
except FileNotFoundError:
    print("Note: CSV file not found. Create './archive/apple.csv' to run this script.")
