# FDA Excel Enhancement Project

## Overview
This project enhances FDA Drug Master File (DMF) Excel data by adding analytical columns to identify China-related pharmaceutical companies and categorize drugs by therapeutic areas.

## Features
- **China Related Detection**: Identifies pharmaceutical companies/holders with Chinese origins
- **Therapeutic Area Classification**: Categorizes base chemicals and drugs into broad therapeutic areas
- **Comprehensive Analysis**: Processes 39,000+ FDA DMF records

## Files Description

### Scripts
- `enhance_fda_excel.py` - Main processing script that adds the analytical columns
- `examine_excel.py` - Utility script to analyze Excel file structure
- `verify_enhanced.py` - Verification script to validate the enhanced data

### Data Files
- `2q2025-excel.xlsx` - Original FDA DMF data (not included due to size)
- `2q2025-excel-enhanced.xlsx` - Enhanced data with added columns (generated)

## Usage

1. **Setup Environment**:
   ```bash
   python3 -m venv excel_env
   source excel_env/bin/activate
   pip install pandas openpyxl
   ```

2. **Place your FDA Excel file** in the project directory as `2q2025-excel.xlsx`

3. **Run the enhancement**:
   ```bash
   python enhance_fda_excel.py
   ```

4. **Verify results**:
   ```bash
   python verify_enhanced.py
   ```

## Results Summary

### China Related Analysis
- **Detection Method**: Pattern matching for Chinese company names, locations, and pharmaceutical indicators
- **Examples**: Shanghai Fourth Pharmaceuticals Ltd, Tianjin Medicines & Health Products
- **Typical Results**: ~9-10% of entries identified as China-related

### Therapeutic Area Categories
- Antibiotics/Anti-infectives
- Vitamins/Nutrients  
- Chemical/Industrial
- Cardiovascular
- Hormones/Endocrine
- Cancer/Oncology
- Anti-inflammatory/Pain
- Central Nervous System
- Blood/Hematological
- Dermatological
- Respiratory
- Gastrointestinal
- Other/Unknown

## Technical Implementation

### China Detection Algorithm
- Searches for Chinese city and province names
- Identifies major Chinese pharmaceutical companies
- Uses regex patterns for Chinese naming conventions
- Recognizes Chinese family names combined with pharmaceutical terms

### Therapeutic Classification
- Keyword-based pattern matching
- Comprehensive therapeutic area dictionaries
- Handles various drug naming conventions
- Fallback categorization for unrecognized substances

## Output
The enhanced Excel file contains all original columns plus:
- **China Related** (Boolean): TRUE/FALSE indicating Chinese origin
- **Therapeutic Area** (String): Broad therapeutic category

## Dependencies
- Python 3.7+
- pandas
- openpyxl

## License
This project is for educational and analytical purposes.