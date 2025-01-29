def main():
    book = "books/frankenstein.txt"
    book_report(book)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    lower_text = text.lower()
    alphabet = {}
    for i in range (0, len(lower_text)):
        if lower_text[i] in alphabet:
            alphabet[lower_text[i]] += 1
        else:
            alphabet[lower_text[i]] = 1
    return alphabet

def convert_dict(dict):
    dict_list = []

    for char, count in dict.items():
        if char.isalpha() == True:
            char_dict = {"char": char, "num": count}
            dict_list.append(char_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["num"]

def book_report(book):
    text = get_book_text(book)
    words = get_word_count(text)
    letters = convert_dict(get_character_count(text))

    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print("")
    for letter in letters:
            print(f"The '{letter["char"]}' character was found {letter["num"]} times")
    print("--- End report ---")

main()