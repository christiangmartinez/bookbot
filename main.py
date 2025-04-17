def get_book_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_list = file_contents.split()
        num_words = len(word_list)
        print(f"{num_words} words found in the document")


def main():
    get_book_word_count('./books/frankenstein.txt')

main()
