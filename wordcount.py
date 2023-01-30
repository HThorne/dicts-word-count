# copied and pasted all from lab worked on with another student

"""Count words in file."""

import sys

def tokenize(file_path):
    """Return list of words from file"""
    
    full_text = open(file_path)
    
    words = []

    for line in full_text:
        words.extend(line.rstrip().split(" "))

    return words

def get_word_count(words):
    """Return dictionary of {word: count} from list"""
    
    word_counts = {}

    for word in words:
        # if word in word_counts:
        #     word_counts[word] = word_counts[word] + 1
        # elif word not in word_counts:
        #     word_counts[word] = 1

        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def print_word_count(word_counts):
    """Print 'words: count' from dictionary"""
    
    for word, count in word_counts.items():
        print(word, count)

def normalized_words(words):
    """Return list of normalized words.

    Words are normalized by removing punctuation and converting letters
    so they're all lowercased.
    """

    normalized = []

    for word in words:
        no_punct_word = ""

        for character in word:
            if character.isalpha():
                no_punct_word += character

        normalized.append(no_punct_word.lower())

    return normalized


file_name = sys.argv[1]
text = tokenize(file_name)
text = normalized_words(text)
word_count = get_word_count(text)

print_word_count(word_count)