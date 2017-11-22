# PROGRAM 1.

import sys

numbers = int(sys.argv[1])
letters = 'TRWAGMYFPDXBNJZSQVHLCKE'

rest = numbers % 23
letter = letters[rest]
print(f"{numbers}{letter}")
