import nltk
import re

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

words_list = [word.lower() for word in words.words()]
names_list = [name.lower() for name in names.words()]


def check_english(proposed_key):
    key_words = proposed_key.split()
    word_count = 0

    for word in key_words:
        word = re.sub(r"[^A-Za-z]+", "", word)
        if word.lower() in words_list or word.lower() in names_list:
            word_count += 1
    return word_count / len(key_words)
