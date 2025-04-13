import sys
from stats import count_words
from stats import count_letters

if len(sys.argv) != 2:
    print("Usage: python3 main.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename) as f:
        text = f.read()
        text = text.replace('\ufeff', '')
        print(count_words(text))
        print(count_letters(text))
except FileNotFoundError:
    print(f"File '{filename}' not found.")


