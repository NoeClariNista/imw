# PROGRAMA 4.

import sys

numero = int(sys.argv[1])

if numero <= 0:
    print("Error.")

else:
    for i in range(1, numero + 1):
        print("Factorial De", i)
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        print("Es", factorial)
