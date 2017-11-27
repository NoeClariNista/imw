# PROGRAM.

import sys


def num_vowels(text):
    VOWELS = "aeiou"
    text = text.lower()
    number = 0
    for vowel in text:
        if vowel in VOWELS:
            number += 1
    return number


def num_whitespaces(text):
    number = 0
    for space in text:
        if space == " ":
            number += 1
    return number


def num_digits(text):
    NUMBERS = "0123456789"
    number = 0
    for number in text:
        if number in NUMBERS:
            number += 1
    return number


def num_words(text):
    text = text.split(" ")
    number_word = len(text)
    return number_word


def reverse(text):
    inverse = text[-1::-1]
    return inverse


def length(text):
    lengh = len(text)
    return lengh


def halfs(text):
    half = len(text) // 2
    first_half = text[:int(half)]
    second_half = text[int(half):]
    return first_half, second_half


def upper_vowels(text):
    VOWELS = "aeiouAEIOU"
    uppertext = ""
    for vowel in text:
        if vowel in VOWELS:
            uppertext += vowel.upper()
        else:
            uppertext += vowel
    return uppertext


def sorted_by_words(text):
    text = text.split(" ")
    sortedtext = sorted(text)
    sortedwords = " ".join(sortedtext)
    return sortedwords


def length_of_words(text):
    text = text.split()
    newlist = list()
    listsize = len(text)
    for i in range(listsize):
        value = len(text[i])
        newlist.append(str(value))
    lengthwords = " ".join(newlist)
    return lengthwords

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
