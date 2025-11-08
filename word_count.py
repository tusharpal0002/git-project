# word_counter.py
import sys
try:
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        print(len(f.read().split()))
except IndexError:
    print("Usage: python word_counter.py <file>")
except FileNotFoundError:
    print("File not found")