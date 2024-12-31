import requests
from bs4 import BeautifulSoup
import argparse
import itertools

# Configure argument parser
parser = argparse.ArgumentParser(
    description="Extract unique terms from a fixed URL based on provided keywords.",
    epilog="Usage examples:\n"
           "  python script.py keyword1 keyword2 --output output.txt\n"
           "  python script.py keyword1 keyword2 keyword3\n",
    formatter_class=argparse.RawTextHelpFormatter
)
parser.add_argument('keywords', metavar='keyword', type=str, nargs='+',
                    help="Keywords to filter the data-term attributes.")
parser.add_argument('--output', metavar='output_path', type=str, default="wordlist.txt",
                    help="Path of the output file (default: wordlist.txt).")
parser.add_argument('--lowercase', action='store_true', help="Convert terms to lowercase.")
parser.add_argument('--uppercase', action='store_true', help="Convert terms to uppercase.")
parser.add_argument('--capitalize', action='store_true', help="Capitalize terms.")
parser.add_argument('--combine', action='store_true', help="Combine terms into permutations.")
parser.add_argument('--add-numbers', metavar='max_num', type=int, default=0,
                    help="Add numbers to terms up to the specified maximum number of digits.")

args = parser.parse_args()

# Base URL to analyze
base_url = "http://relatedwords.io/"

# Keywords to use for generating the wordlist
keywords = args.keywords

# Path of the output file
output_path = args.output

# Set to store unique terms
data_terms = set()

# Fetch the page content for each keyword and extract relevant terms
for keyword in keywords:
    full_url = f"{base_url}{keyword}"
    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for li in soup.find_all('li'):
        term = li.get('data-term')
        if term:
            data_terms.update(term.split())


# Generate lowercase
def lowercase(words):
    wordlist = set()
    
    for word in words:
        wordlist.add(word.lower())

    return wordlist


# Generate uppercase
def uppercase(words):
    wordlist = set()
    
    for word in words:
        wordlist.add(word.upper())

    return wordlist

# Generate capitaze
def capitalize(words):
    wordlist = set()
    
    for word in words:
        wordlist.add(word.capitalize())

    return wordlist

# Generate combinations
def combine(words):
    wordlist = set()

    for combo in itertools.permutations(words, 2):
        wordlist.add(''.join(combo))
    
    return wordlist

def add_numbers(words, max_num=2):
    wordlist = set()

    # Add numbers to the end
    for word in list(words):
        for num in range(1, 10**max_num):
            wordlist.add(f"{word}{num}")

    return wordlist

final_wordlist = data_terms.copy()

if args.lowercase:
    final_wordlist.update(lowercase(data_terms))
if args.uppercase:
    final_wordlist.update(uppercase(data_terms))
if args.capitalize:
    final_wordlist.update(capitalize(data_terms))
if args.combine:
    final_wordlist.update(combine(data_terms))
if args.add_numbers > 0:
    final_wordlist.update(add_numbers(data_terms, args.add_numbers))

# Save the results to a txt file
with open(output_path, "w") as file:
    for term in sorted(final_wordlist):
        file.write(term + "\n")

# Display success message
print(f"{len(final_wordlist)} unique terms have been saved in '{output_path}'. Keywords applied: {', '.join(keywords)}.")
