# PROGRAM 3.

import sys

number = int(sys.argv[1])
words = sys.argv[2]
accountant = 0

if (number <= 0):
    print("Error.")
else:
    words = words.split(" ")
    for i in words:
        if (len(i) == number):
            accountant += 1
    print("Hay", accountant, "Palabras De Tamaño", number)
