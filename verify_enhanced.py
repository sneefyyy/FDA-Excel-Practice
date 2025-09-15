#!/usr/bin/env python3
"""
FDA Excel Enhancement Verification Script

This script verifies the enhanced Excel file and displays statistics
about the added analytical columns.
"""

import pandas as pd

def verify_enhanced_file(filename):
    """Verify the enhanced Excel file"""
    try:
        df = pd.read_excel(filename)
        
        print(f"Enhanced file shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        
        print(f"\nFirst 5 rows:")
        print(df[['HOLDER', 'SUBJECT', 'China Related', 'Therapeutic Area']].head())
        
        # China Related Analysis
        china_count = df['China Related'].sum()
        total_count = len(df)
        print(f"\n" + "="*60)
        print("CHINA RELATED ANALYSIS")
        print("="*60)
        print(f"Total China-related entries: {china_count} out of {total_count} ({china_count/total_count*100:.1f}%)")
        
        # Show some China-related examples
        china_examples = df[df['China Related'] == True].head(10)
        if not china_examples.empty:
            print(f"\nSample China-related entries:")
            for idx, row in china_examples.iterrows():
                print(f"  • {row['HOLDER']}")
                print(f"    Subject: {row['SUBJECT']}")
                print(f"    Therapeutic Area: {row['Therapeutic Area']}")
                print()
        
        # Therapeutic Area Analysis
        print("="*60)
        print("THERAPEUTIC AREA ANALYSIS")
        print("="*60)
        print(f"Therapeutic Area distribution:")
        area_counts = df['Therapeutic Area'].value_counts()
        for area, count in area_counts.items():
            percentage = count/len(df)*100
            print(f"  {area:.<35} {count:>6} ({percentage:>5.1f}%)")
        
        # Show some specific therapeutic examples
        print(f"\n" + "="*60)
        print("SAMPLE ENTRIES BY THERAPEUTIC AREA")
        print("="*60)
        for area in ['Antibiotics/Anti-infectives', 'Vitamins/Nutrients', 'Hormones/Endocrine', 'Cancer/Oncology']:
            examples = df[df['Therapeutic Area'] == area]['SUBJECT'].head(3).tolist()
            if examples:
                print(f"\n{area}:")
                for i, example in enumerate(examples, 1):
                    print(f"  {i}. {example}")
        
        # Cross-analysis: China + Therapeutic Areas
        print(f"\n" + "="*60)
        print("CHINA-RELATED ENTRIES BY THERAPEUTIC AREA")
        print("="*60)
        china_therapeutic = df[df['China Related'] == True]['Therapeutic Area'].value_counts()
        if not china_therapeutic.empty:
            for area, count in china_therapeutic.head(10).items():
                percentage = count/china_count*100
                print(f"  {area:.<35} {count:>6} ({percentage:>5.1f}%)")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import os
    filename = "2q2025-excel-enhanced.xlsx"
    
    if not os.path.exists(filename):
        print(f"Error: Enhanced file '{filename}' not found.")
        print("Please run 'enhance_fda_excel.py' first to create the enhanced file.")
    else:
        verify_enhanced_file(filename)