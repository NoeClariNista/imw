# PROGRAM.

import sys


def num_vowels(text):
    vowels = 'aeiou'
    text = text.lower()
    num = 0
    for i in text:
        if i in vowels:
            num += 1
    return num


def num_whitespaces(text):
    num = 0
    for i in text:
        if i == " ":
            num += 1
    return num


def num_digits(text):
    numbers = '0123456789'
    num = 0
    for i in text:
        if i in numbers:
            num += 1
    return num


def num_words(text):
    text = text.split(" ")
    nw = len(text)
    return nw


def reverse(text):
    inv = text[-1::-1]
    return inv


def length(text):
    l = len(text)
    return l


def halfs(text):
    half = len(text) // 2
    first_half = text[:int(half)]
    second_half = text[int(half):]
    return first_half, second_half


def upper_vowels(text):
    vowels = 'aeiouAEIOU'
    utext = ""
    for vowel in text:
        if vowel in vowels:
            utext += vowel.upper()
        else:
            utext += vowel
    return utext


def sorted_by_words(text):
    text = text.split(" ")
    textsorted = sorted(text)
    sbw = " ".join(textsorted)
    return sbw


def length_of_words(text):
    text = text.split()
    newlist = list()
    listsize = len(text)
    for i in range(listsize):
        value = len(text[i])
        newlist.append(str(value))
    low = " ".join(newlist)
    return low

text = sys.argv[1]
print("Number of vowels: ", num_vowels(text))
print("Number of whitespaces: ", num_whitespaces(text))
print("Number of digits: ", num_digits(text))
print("Number of words: ", num_words(text))
print("Reverse of text: ", reverse(text))
print("Length of text: ", length(text))
print("Halfs of text: ", " | ".join(halfs(text)))
print("Text with uppercased vowels: ", upper_vowels(text))
print("Sorted by words: ", sorted_by_words(text))
print("Length of words: ", length_of_words(text))
