from stats import count_words, count_char, report
import sys

args = sys.argv[1:]
if len(args) != 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
code=open(args[0]).read()

print(count_words(code))
print(count_char(code))

report(code)