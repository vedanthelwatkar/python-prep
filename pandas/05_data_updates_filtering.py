"""
Pandas: Data Updates and Filtering
Updating values and boolean filtering in DataFrames
"""

import pandas as pd

# Load CSV file (assuming the archive folder exists)
try:
    df = pd.read_csv('./archive/apple.csv')
    
    print("=" * 50)
    print("Data Updates and Filtering")
    print("=" * 50)
    
    print("\nUpdate using loc (label-based):")
    print("df.loc[9, 'year'] = 2026")
    df.loc[9, 'year'] = 2026
    
    print("\nUpdate using iloc (position-based):")
    print("df.iloc[8, 2] = 2026")
    df.iloc[8, 2] = 2026
    
    print("\nBoolean Filtering:")
    print("df[df['year'] == 2026]:")
    result = df[df['year'] == 2026]
    print(result)
    
except FileNotFoundError:
    print("Note: CSV file not found. Create './archive/apple.csv' to run this script.")
