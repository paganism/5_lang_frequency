from collections import Counter
import sys
import re


def load_data(filepath):
    with open(filepath, 'r') as file:
        raw_data = file.read()
    return raw_data


def get_most_frequent_words(text):
    count_to_output = 10
    clean_list = re.findall(r'\w+', text)
    return Counter(clean_list).most_common(count_to_output)


if __name__ == '__main__':
    filepath = sys.argv[1]
    for word, count in get_most_frequent_words(load_data(filepath)):
        print("{} {}".format(word, count))
