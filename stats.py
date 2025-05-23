def count_words(text):
    return (len(text.split()))


def count_char(text):
    chars={}
    for value in text.lower():
        char=value
        chars[value] = chars.get(value, 0) + 1
    return chars


def report(code):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Found {count_words(code)} total words in the document")
    for char,value in count_char(code).items():
        print(f"{char}: {value} ")