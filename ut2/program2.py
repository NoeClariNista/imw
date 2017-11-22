# PROGRAM 2.

import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

a = 0
g = 0
c = 0
t = 0

for i in range(0, DNA_SIZE):
    if (sequence[i] == "A"):
        a += 1
    elif (sequence[i] == "G"):
        g += 1
    elif (sequence[i] == "C"):
        c += 1
    else:
        t += 1
print("Adenine:", a, "\nGuanine:", g, "\nCytosine:", c, "\nThymine:", t)
