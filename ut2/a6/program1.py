# PROGRAM 1.

import sys


def count_words(sentence):
    summary = {}
    words = sentence.split()
    for word in words:
        if word not in summary:
            summary[word] = 1
        else:
            summary[word] += 1
    return summary

sentence = sys.argv[1]

for word, count in (count_words(sentence).items()):
    print(f"{word}: {count}")
