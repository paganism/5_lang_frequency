from collections import Counter
import sys

filepath = sys.argv[1]


def load_data(filepath):
    with open(filepath, 'r') as f:
        raw_data = f.read().split()
    return raw_data


def get_most_frequent_words(text):
    clean_data = []
    for word in text:
        clean_data.append(word.strip(',.!-'))
    return Counter(text).most_common(10)


if __name__ == '__main__':
    print(get_most_frequent_words(load_data("textfile.txt")))
