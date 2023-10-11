# Email Extractor

This is a Python script that extracts email addresses from CSV files and saves them to a new CSV file while giving you the option to choose between extracting all emails or just one email per domain.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)
- [License](#license)

## Installation

1. Clone this repository to your local machine using `git clone`.
2. Make sure you have Python 3.x installed on your system.

## Usage

1. Place your input CSV files in the 'inputs' folder.
2. Open your terminal and navigate to the project directory.
3. Run the script:

   ```bash
   python email-extractor.py
4. You will be prompted to choose whether you want to extract all emails or just one email per domain.
5. The script will process the input files, extract the email addresses, and save them in the 'outputs' folder with a unique timestamp appended to the filename.
6. The number of found email addresses will be displayed in the terminal for each input file.

## Options
When prompted to check for emails, you can enter "yes" to extract all email addresses or "no" to extract one email per domain.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
