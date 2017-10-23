from collections import Counter
import sys


def load_data(filepath):
    with open(filepath, 'r') as f:
        raw_data = f.read()
    return raw_data


def get_most_frequent_words(text):
    count_to_output = 10
    splitted_text = text.split()
    clean_data = []
    for word in text:
        clean_data.append(word.strip(',.!-[]()*/{}+=<>?&^$#@~`;:'))
    return Counter(splitted_text).most_common(count_to_output)


if __name__ == '__main__':
    filepath = sys.argv[1]
    for resultdata in range(len(get_most_frequent_words(load_data(filepath)))):
        print("Слово: ", get_most_frequent_words(load_data(filepath))[resultdata][0], "количество повторений: ", get_most_frequent_words(load_data(filepath))[resultdata][1])
