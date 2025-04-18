def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_char_count(text):
    chars = {}

    for c in text:
        letter = c.lower()
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1

    return chars


def get_sorted_char_count(chars):
    char_list = []

    for char in chars:
        new_dict = { char: chars[char] }
        char_list.append(new_dict)

    char_list.sort()
    for letter in char_list:
        if letter.isalpha():
            print(letter)

