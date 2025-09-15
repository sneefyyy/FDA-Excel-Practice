#!/bin/bash
# FDA Excel Enhancement Setup Script

echo "Setting up FDA Excel Enhancement Environment..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv excel_env

# Activate virtual environment
echo "Activating virtual environment..."
source excel_env/bin/activate

# Install requirements
echo "Installing Python packages..."
pip install -r requirements.txt

echo ""
echo "Setup completed successfully!"
echo ""
echo "To use the enhancement tools:"
echo "1. Place your FDA Excel file as '2q2025-excel.xlsx' in this directory"
echo "2. Run: source excel_env/bin/activate"
echo "3. Run: python enhance_fda_excel.py"
echo "4. Verify results: python verify_enhanced.py"
echo ""
echo "The enhanced file will be saved as '2q2025-excel-enhanced.xlsx'"