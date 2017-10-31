from collections import Counter
import sys
import re


def load_data(filepath):
    with open(filepath, 'r') as f:
        raw_data = f.read()
    return raw_data


def get_most_frequent_words_re(text):
    count_to_output = 10
    clean_list = re.findall(r'\w+', text)
    print(clean_list)
    return Counter(clean_list).most_common(count_to_output)


if __name__ == '__main__':
    filepath = sys.argv[1]
    for item in get_most_frequent_words_re(load_data(filepath)):
        print(item[0], "repeated ", item[1], "times")
