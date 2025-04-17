def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        word_list = file_contents.split()
        num_words = len(word_list)
        print(f"{num_words} words found in the document")

def get_char_count(filepath):
    with open(filepath) as f:
        file_contents = f.read().lower()
        letters = list(file_contents)

        chars = {}

        for letter in letters:
            if letter in chars:
                chars[letter] += 1
            else:
                chars[letter] = 1

        for char in chars:
            count = chars[char]
            print(f"'{char}': {count}")

