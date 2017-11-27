# PROGRAM.

import sys


def num_vowels(text):
    VOWELS = "aeiou"
    text = text.lower()
    number_vowels = 0
    for vowel in text:
        if vowel in VOWELS:
            number_vowels += 1
    return number_vowels


def num_whitespaces(text):
    number_whitespaces = 0
    for space in text:
        if space == " ":
            number_whitespaces += 1
    return number_whitespaces


def num_digits(text):
    NUMBERS = "0123456789"
    number_digits = 0
    for number in text:
        if number in NUMBERS:
            number_digits += 1
    return number_digits


def num_words(text):
    text = text.split(" ")
    number_words = len(text)
    return number_words


def reverse(text):
    inverse = text[-1::-1]
    return inverse


def length(text):
    lengt = len(text)
    return lengt


def halfs(text):
    half = len(text) // 2
    first_half = text[:int(half)]
    second_half = text[int(half):]
    return first_half, second_half


def upper_vowels(text):
    VOWELS = "aeiouAEIOU"
    upper_text = ""
    for vowel in text:
        if vowel in VOWELS:
            upper_text += vowel.upper()
        else:
            upper_text += vowel
    return upper_text


def sorted_by_words(text):
    text = text.split(" ")
    sorted_text = sorted(text)
    sorted_words = " ".join(sorted_text)
    return sorted_words


def length_of_words(text):
    text = text.split()
    new_list = list()
    list_size = len(text)
    for i in range(list_size):
        value = len(text[i])
        new_list.append(str(value))
    length_words = " ".join(new_list)
    return length_words

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
