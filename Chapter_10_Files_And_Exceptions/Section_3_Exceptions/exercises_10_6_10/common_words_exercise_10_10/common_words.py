from pathlib import Path


def count_words(filename):
    """Function to count words in a text"""
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exists.")
    else:
        # Count the approximate number of the words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def count_amount_words_specific(filename, word):
    """Count the amount of times a specific words appears in a text"""
    path = Path(filename)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exists.")
    else:
        # Count the approximate number of the words in the file:
        words = contents.split()
        specific_word = words.count(word)
        print(f"The file {filename} has about {specific_word} times the word {word}.")


count_amount_words_specific('metamorphosis.txt', 'the')