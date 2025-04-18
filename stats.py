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
        if char.isalpha():
            char_list.append({"character": char, "count": chars[char]})

    char_list.sort(reverse=True, key=sort_on)

    return char_list

def sort_on(dict):
    return dict["count"]
