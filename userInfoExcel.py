import pandas as pd
import json

from openpyxl.workbook import Workbook

# Read the JSON file
with open('users.json', 'r') as file:
    users = json.load(file)

# Convert JSON data to a DataFrame
df = pd.DataFrame(users)

# Define the Excel file path
excel_file = 'data.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(excel_file, index=False)

print(f'Excel file "{excel_file}" has been created successfully.')