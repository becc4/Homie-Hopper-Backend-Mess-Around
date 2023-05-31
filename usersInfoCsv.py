import csv
import json

def userInfoCsv():
# Read the JSON file
    with open('users.json', 'r') as file:
        users = json.load(file)

    # Define the CSV file path
    csv_file = 'grid.csv'

    # Extract the field names from the first user
    field_names = list(users[0].keys())

    # Write the data to CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(users)

    return csv_file


