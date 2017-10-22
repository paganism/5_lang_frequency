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
    for i in get_most_frequent_words(load_data(filepath)):
        print("слово: ",i,"количество повторений: ")
    #print(get_most_frequent_words(load_data(filepath))[0][0])
