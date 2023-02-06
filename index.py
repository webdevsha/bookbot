book_path = "books/frankenstein.txt"

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_character_sums(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(book_path) as f:
        return f.read()

def generate_letter_report(text):
    # Create a dictionary to store the count of each letter
    letter_count = {}
    for letter in text:
        # Ignore whitespace and punctuation
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    # Sort the dictionary by letter
    sorted_letter_count = dict(sorted(letter_count.items()))
    # Print the report
    print("Letter Report for Frankenstein:")
    for letter, count in sorted_letter_count.items():
        print(f"{letter}: {count}")

def count_word(text, word):
    word_count = 0
    for i in range(len(text) - len(word) + 1):
        if text[i:i+len(word)].lower() == word.lower():
            word_count += 1
    return word_count

text = get_book_text(book_path)
word_count = count_word(text, "ugly")

print("The word 'ugly' appears", word_count, "times in the text.")
generate_letter_report(text)

