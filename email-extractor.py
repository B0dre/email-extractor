import csv
import re
import os
from datetime import datetime

# Function to extract email addresses from a string
def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.findall(email_pattern, text)

# Input folder and output folder paths
input_folder = 'inputs'
output_folder = 'outputs'

# Ask the user if they want to check for all emails or just one email per domain
check_all_emails = input("Do you want to check for all emails ((y)yes/no)? ").strip().lower() == 'yes' or 'y'

# Get the list of CSV files in the input folder
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

# Process each CSV file in the input folder
for input_file in csv_files:
    input_path = os.path.join(input_folder, input_file)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_file = f'{os.path.splitext(input_file)[0]}_found-emails_{timestamp}.csv'
    output_path = os.path.join(output_folder, output_file)

    # Read the input CSV file and extract email addresses
    found_emails = set()
    found_domains = set()

    with open(input_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for cell in row:
                emails = extract_emails(cell)
                for email in emails:
                    if check_all_emails or email.split('@')[1] not in found_domains:
                        found_emails.add(email)
                        found_domains.add(email.split('@')[1])

    # Save the found email addresses to the output CSV file
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for email in found_emails:
            writer.writerow([email])

    # Display the number of found email addresses and the output file path
    print(f"Found {len(found_emails)} email addresses. Saved to {output_path}")
