#!/usr/bin/env python3
"""
FDA Excel Enhancement Script

This script processes FDA Drug Master File (DMF) Excel data and adds two analytical columns:
1. China Related - Identifies Chinese pharmaceutical companies/holders
2. Therapeutic Area - Categorizes drugs by broad therapeutic areas

Author: GitHub Copilot CLI
Date: September 2024
"""

import pandas as pd
import re
import numpy as np

def is_china_related(holder_name):
    """
    Determine if a company/holder name is China-related based on naming patterns
    
    Args:
        holder_name (str): Company/holder name to analyze
        
    Returns:
        bool: True if China-related, False otherwise
    """
    if pd.isna(holder_name) or not isinstance(holder_name, str):
        return False
    
    holder_lower = holder_name.lower()
    
    # Common Chinese company indicators
    chinese_indicators = [
        'china', 'chinese', 'beijing', 'shanghai', 'guangzhou', 'shenzhen',
        'tianjin', 'chongqing', 'wuhan', 'nanjing', 'hangzhou', 'suzhou',
        'xiamen', 'dalian', 'qingdao', 'jinan', 'changsha', 'zhengzhou',
        'hefei', 'kunming', 'urumqi', 'lanzhou', 'xian', 'chengdu',
        'hunan', 'hubei', 'guangdong', 'zhejiang', 'jiangsu', 'shandong',
        'hebei', 'henan', 'anhui', 'fujian', 'liaoning', 'jilin',
        'heilongjiang', 'inner mongolia', 'xinjiang', 'tibet', 'ningxia',
        'gansu', 'qinghai', 'yunnan', 'guizhou', 'sichuan', 'chongqing',
        'sinopharm', 'sinopec', 'petrochina', 'cnooc', 'cofco',
        'sinochem', 'chemchina', 'cnpc'
    ]
    
    # Common Chinese pharmaceutical company patterns
    chinese_pharma_patterns = [
        r'\b(sino|china|chinese)\b.*\b(pharm|pharma|pharmaceutical|medicine|medical|bio|chemical)\b',
        r'\b(pharm|pharma|pharmaceutical|medicine|medical|bio|chemical)\b.*\b(sino|china|chinese)\b',
        r'\b\w+\s+(pharma|pharmaceutical)\s+(china|chinese)\b',
        r'\bchina\s+\w+\s+(pharm|pharma|pharmaceutical|medicine|medical|bio|chemical)\b'
    ]
    
    # Check for direct Chinese indicators
    for indicator in chinese_indicators:
        if indicator in holder_lower:
            return True
    
    # Check for Chinese pharmaceutical patterns
    for pattern in chinese_pharma_patterns:
        if re.search(pattern, holder_lower):
            return True
    
    # Common Chinese naming patterns (family names + company structure)
    chinese_name_patterns = [
        r'\b(wang|li|zhang|liu|chen|yang|huang|zhao|wu|zhou|xu|sun|ma|zhu|hu|guo|he|lin|luo|zheng|liang|xie|song|tang|feng|han|cao|peng|zeng|xiao|tian|dong|pan|ye|cheng|yu|yuan|jiang|cui|jin|wei|du|shi|fan|fang|lu|dai|xia|zhong|qiu|hou|zou|long|duan|shen|meng)\s+(pharm|pharma|pharmaceutical|medicine|medical|bio|chemical|lab|laboratories|corp|company|co|ltd|inc)\b'
    ]
    
    for pattern in chinese_name_patterns:
        if re.search(pattern, holder_lower):
            return True
    
    return False

def categorize_therapeutic_area(subject):
    """
    Categorize the chemical/drug into broad therapeutic areas based on the subject name
    
    Args:
        subject (str): Drug/chemical name to categorize
        
    Returns:
        str: Therapeutic area category
    """
    if pd.isna(subject) or not isinstance(subject, str):
        return "Unknown"
    
    subject_lower = subject.lower()
    
    # Define therapeutic area patterns
    therapeutic_patterns = {
        "Antibiotics/Anti-infectives": [
            'penicillin', 'streptomycin', 'tyrothricin', 'antibiotic', 'antimicrobial',
            'bactericidal', 'bacteriostatic', 'sulfathiazole', 'sulfonamide',
            'tetracycline', 'erythromycin', 'ampicillin', 'amoxicillin', 'cephalosporin',
            'quinolone', 'fluoroquinolone', 'macrolide', 'lincomycin', 'clindamycin',
            'vancomycin', 'rifampin', 'isoniazid', 'antifungal', 'antiviral'
        ],
        
        "Vitamins/Nutrients": [
            'vitamin', 'riboflavin', 'thiamine', 'niacin', 'biotin', 'folic acid',
            'cobalamin', 'ascorbic acid', 'tocopherol', 'retinol', 'calciferol',
            'amino acid', 'protein hydrolysate', 'mineral', 'calcium', 'iron',
            'zinc', 'magnesium', 'potassium', 'sodium', 'phosphorus'
        ],
        
        "Hormones/Endocrine": [
            'hormone', 'progesterone', 'estrogen', 'testosterone', 'cortisol',
            'insulin', 'thyroid', 'thyroxine', 'adrenaline', 'epinephrine',
            'norepinephrine', 'growth hormone', 'prolactin', 'oxytocin',
            'vasopressin', 'steroid', 'corticosteroid', 'glucocorticoid'
        ],
        
        "Cancer/Oncology": [
            'nitrogen mustard', 'antineoplastic', 'chemotherapy', 'cytotoxic',
            'alkylating', 'mitomycin', 'adriamycin', 'bleomycin', 'cisplatin',
            'carboplatin', 'paclitaxel', 'docetaxel', 'vincristine', 'vinblastine',
            'methotrexate', 'fluorouracil', 'cyclophosphamide', 'oncology'
        ],
        
        "Cardiovascular": [
            'cardiac', 'cardio', 'heart', 'digitalis', 'digoxin', 'quinidine',
            'propranolol', 'atenolol', 'metoprolol', 'verapamil', 'nifedipine',
            'amlodipine', 'enalapril', 'lisinopril', 'losartan', 'warfarin',
            'heparin', 'aspirin', 'clopidogrel', 'statin', 'antihypertensive'
        ],
        
        "Central Nervous System": [
            'neurological', 'neuro', 'brain', 'central nervous', 'cns',
            'antidepressant', 'antipsychotic', 'anxiolytic', 'sedative',
            'hypnotic', 'anticonvulsant', 'antiepileptic', 'analgesic',
            'anesthetic', 'morphine', 'codeine', 'barbiturate', 'benzodiazepine',
            'phenytoin', 'carbamazepine', 'valproic acid', 'lithium'
        ],
        
        "Gastrointestinal": [
            'gastric', 'stomach', 'intestinal', 'digestive', 'antacid',
            'proton pump inhibitor', 'h2 blocker', 'antiemetic', 'laxative',
            'antidiarrheal', 'inflammatory bowel', 'ulcer', 'peptic'
        ],
        
        "Respiratory": [
            'respiratory', 'lung', 'bronchial', 'asthma', 'bronchodilator',
            'corticosteroid inhaled', 'beta agonist', 'anticholinergic',
            'expectorant', 'antitussive', 'decongestant', 'antihistamine'
        ],
        
        "Anti-inflammatory/Pain": [
            'anti-inflammatory', 'antiinflammatory', 'nsaid', 'ibuprofen',
            'naproxen', 'diclofenac', 'indomethacin', 'celecoxib', 'pain',
            'analgesic', 'arthritis', 'rheumatic', 'rheumatoid'
        ],
        
        "Dermatological": [
            'dermatological', 'skin', 'topical', 'dermatitis', 'eczema',
            'psoriasis', 'acne', 'antifungal topical', 'corticosteroid topical'
        ],
        
        "Blood/Hematological": [
            'blood', 'hematological', 'anemia', 'coagulation', 'anticoagulant',
            'blood substitute', 'plasma', 'serum', 'hemoglobin', 'iron deficiency',
            'thrombosis', 'hemophilia', 'platelet'
        ],
        
        "Chemical/Industrial": [
            'cpc', 'cellulose', 'polymer', 'solvent', 'preservative',
            'excipient', 'filler', 'binder', 'coating', 'tablet', 'capsule',
            'gelatin', 'starch', 'lactose', 'microcrystalline cellulose'
        ]
    }
    
    # Check each therapeutic area
    for area, keywords in therapeutic_patterns.items():
        for keyword in keywords:
            if keyword in subject_lower:
                return area
    
    # Special case for very short or unclear subjects
    if len(subject_lower) <= 3:
        return "Unknown"
    
    return "Other"

def process_fda_excel(input_filename, output_filename):
    """
    Process the FDA Excel file and add the two requested columns
    
    Args:
        input_filename (str): Path to input Excel file
        output_filename (str): Path to output Excel file
        
    Returns:
        pandas.DataFrame: Processed dataframe with new columns
    """
    try:
        # Read the Excel file
        df = pd.read_excel(input_filename, sheet_name=0, header=0)
        
        # Fix the headers (use first row as column names)
        if len(df.columns) > 0 and 'DMF#' in str(df.iloc[0].values):
            new_columns = df.iloc[0].values
            df = df[1:]  # Remove the header row from data
            df.columns = new_columns
            df = df.reset_index(drop=True)
        
        print(f"Original DataFrame shape: {df.shape}")
        
        # Add China Related column
        print("Adding 'China Related' column...")
        df['China Related'] = df['HOLDER'].apply(is_china_related)
        
        # Add Therapeutic Area column
        print("Adding 'Therapeutic Area' column...")
        df['Therapeutic Area'] = df['SUBJECT'].apply(categorize_therapeutic_area)
        
        print(f"Final DataFrame shape: {df.shape}")
        
        # Show some statistics
        china_count = df['China Related'].sum()
        print(f"\nChina-related entries: {china_count} out of {len(df)} ({china_count/len(df)*100:.1f}%)")
        
        print(f"\nTherapeutic Area distribution:")
        area_counts = df['Therapeutic Area'].value_counts()
        for area, count in area_counts.head(10).items():
            print(f"  {area}: {count} ({count/len(df)*100:.1f}%)")
        
        # Show some examples of China-related entries
        china_examples = df[df['China Related'] == True][['HOLDER', 'SUBJECT']].head(10)
        if not china_examples.empty:
            print(f"\nSample China-related entries:")
            for idx, row in china_examples.iterrows():
                print(f"  {row['HOLDER']} - {row['SUBJECT']}")
        
        # Save to new Excel file
        df.to_excel(output_filename, index=False, sheet_name='FDA_DMF_Enhanced')
        print(f"\nEnhanced data saved to: {output_filename}")
        
        return df
        
    except Exception as e:
        print(f"Error processing Excel file: {e}")
        return None

if __name__ == "__main__":
    input_file = "2q2025-excel.xlsx"
    output_file = "2q2025-excel-enhanced.xlsx"
    
    # Check if input file exists
    import os
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        print("Please place your FDA Excel file in the same directory as this script.")
        exit(1)
    
    # Process the file
    df = process_fda_excel(input_file, output_file)
    
    if df is not None:
        print("\n" + "="*50)
        print("Enhancement completed successfully!")
        print("="*50)