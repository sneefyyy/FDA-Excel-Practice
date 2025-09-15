#!/usr/bin/env python3
"""
FDA Excel Structure Examination Script

This utility script examines the structure of FDA Excel files to understand
the data format and column layout.
"""

import pandas as pd

def examine_excel_structure(filename):
    """Examine the structure of the Excel file"""
    try:
        # Read the Excel file with the first row as headers
        df = pd.read_excel(filename, sheet_name=0, header=0)
        
        # The actual headers are in the first row, so let's use them
        if len(df.columns) > 0 and 'DMF#' in str(df.iloc[0].values):
            # Use the first row as column names
            new_columns = df.iloc[0].values
            df = df[1:]  # Remove the header row from data
            df.columns = new_columns
            df = df.reset_index(drop=True)
        
        print(f"DataFrame shape: {df.shape}")
        print(f"Column names: {list(df.columns)}")
        print(f"\nFirst few rows:")
        print(df.head())
        
        # Look for the 'SUBJECT' column
        if 'SUBJECT' in df.columns:
            print(f"\nSample 'SUBJECT' values:")
            print(df['SUBJECT'].head(20))
            print(f"\nUnique SUBJECT values count: {df['SUBJECT'].nunique()}")
        else:
            print(f"\n'SUBJECT' column not found. Available columns: {list(df.columns)}")
        
        # Also show HOLDER column for Chinese company detection
        if 'HOLDER' in df.columns:
            print(f"\nSample 'HOLDER' values:")
            print(df['HOLDER'].head(20))
        
        return df
        
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

if __name__ == "__main__":
    import os
    filename = "2q2025-excel.xlsx"
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        print("Please place your FDA Excel file in the same directory as this script.")
    else:
        df = examine_excel_structure(filename)