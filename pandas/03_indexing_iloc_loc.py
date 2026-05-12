"""
Pandas: Indexing with iloc and loc
Position-based (iloc) and label-based (loc) indexing
"""

import pandas as pd

# Load CSV file (assuming the archive folder exists)
try:
    df = pd.read_csv('./archive/apple.csv')
    
    print("=" * 50)
    print("iloc vs loc Indexing")
    print("=" * 50)
    
    series = df['year']
    
    print("\nSeries iloc indexing (position-based):")
    print("series.iloc[5:10] =")
    print(series.iloc[5:10])
    
    print("\nSeries loc indexing (label-based):")
    print("series.loc[9] =", series.loc[9])
    
    print("\nDataFrame iloc indexing (rows and columns by position):")
    print("df.iloc[[3, 5], [8, 9]] =")
    print(df.iloc[[3, 5], [8, 9]])
    
    print("\nDataFrame loc indexing (rows and columns by label):")
    print("df.loc[[3, 7], ['year', 'month']] =")
    print(df.loc[[3, 7], ['year', 'month']])
    
except FileNotFoundError:
    print("Note: CSV file not found. Create './archive/apple.csv' to run this script.")
