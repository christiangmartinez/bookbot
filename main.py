import sys

from stats import get_char_count, get_num_words, get_sorted_char_count


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = (sys.argv[1])
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_count(text)
    sorted_chars = get_sorted_char_count(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in sorted_chars:
        print(f'{char["character"]}: {char["count"]}')

    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()

