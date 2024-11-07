code=open("books/frankenstein.txt").read()

def count_words(text):
    return (len(text.split()))

print(count_words(code))

def count_char(text):
    chars={}
    for value in text.lower():
        char=value
        chars[value] = chars.get(value, 0) + 1
    return chars

print(count_char(code))

def report(code):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(code)} found in the document")
    for char,value in count_char(code).items():
        print(f"The '{char}' character was found {value} times")
report(code)