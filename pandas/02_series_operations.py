"""
Pandas: Series Operations
Working with Pandas Series and basic indexing
"""

import pandas as pd

# Load CSV file (assuming the archive folder exists)
try:
    df = pd.read_csv('./archive/apple.csv')
    
    print("=" * 50)
    print("Series Operations")
    print("=" * 50)
    
    # Create a series
    series = df['year']
    
    print("\nType of Single Column (Series):")
    print("type(df['year']) =", type(series))
    
    print("\nType of Multiple Columns (DataFrame):")
    print("type(df[['year', 'month']]) =", type(df[['year', 'month']]))
    
    print("\nAccessing element by index:")
    print("series[9] =", series[9])
    
    print("\nReplacing value in series:")
    series[9] = 2026
    print("series[9] = 2026 =>", series[9])
    
except FileNotFoundError:
    print("Note: CSV file not found. Create './archive/apple.csv' to run this script.")
