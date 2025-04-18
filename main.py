from stats import get_char_count, get_num_words, get_sorted_char_count


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)
    #get_sorted_char_count(chars_dict)
    print(f"{num_words} words found in the document")
    print(chars_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
