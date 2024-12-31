# wordlister
 `Flexible Keyword-Based Wordlist Generator`

A Python script designed for extracting, transforming, and generating wordlists based on keywords from a fixed URL. The script supports multiple customizations, such as case transformations, combining terms, and appending numbers. It's a versatile tool for creating wordlists tailored for specific use cases, including security testing, data processing, or automation tasks.

## Features
- **Case Transformation:** Convert terms to lowercase, uppercase, or capitalize them.
- **Combining Terms:** Create permutations of the extracted terms.
- **Appending Numbers:** Add numerical sequences to the terms.
- **Custom Output File:** Save the generated wordlist to a specified file.

## Usage

`python3 wordlister.py <keywords> [--combine] [--capitalize] [--add-numbers <digits>] [--output <output filename>]`

### Options

| Option | Description |
|--------|-------------|
|--output|Specify the output file path (default: wordlist.txt)|
|--lowercase|Convert terms to lowercase|
|--uppercase|Convert terms to uppercase|
|--capitalize|Capitalize terms|
|--combine|Combine terms into permutations|
|--add-numbers <digits>|Add numbers to terms (e.g., --add-numbers 3 for 3 digits)|

## Examples
### Example 1. Generate a wordlist related to *cars*
    python3 wordlister.py cars

### Example 2. Generate a wordlist related to *cars* with capitalize
    python3 wordlister.py cars --capitalize

### Example 3. Generate a wordlist related to *cars* and combine the terms
    python3 wordlister.py cars --combine

### Example 1. Generate a wordlist related to *cars*, append numbers up to 3 digits and save to *wordlist_test.txt*
    python3 wordlister.py cars --add-numbers 3 --output wordlist_test.txt

## Requirements
To use this script, ensure the following dependencies are installed on your system:
- Python: Version 3.6 or higher.

        sudo apt-get install python3

- Libraries:
  - `requests`
  - `beautifulsoup4`

        pip install request beatifulsoup4

*Permissions: Sufficient privileges to run network scans (e.g., sudo access if required).*
