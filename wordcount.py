"""Count words in file."""

import re, sys

def tokenize(filename):
    data = open(filename)
    words = []
    
    for line in data:
        line_lst = line.strip().split(' ')
        for word in line_lst:
            normalize = word
            normalize = re.sub(r'[^\w\s]','', normalize.lower())
            words.append(normalize)
    
    return words

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

def print_word_counts(word_counts):
    for word, count in word_counts.items():
        print(word, count)

words = tokenize(sys.argv[1])
word_counts = count_words(words)
print_word_counts(word_counts)

