# PROGRAMA 1.

import sys

numero = int(sys.argv[1])

if numero <= 0:
    print("Error.")

else:
    for i in range(2, numero):
        if (numero % i == 0):
            print("El Numero No Es Primo")
            break
    else:
        print ("El Numero Es Primo.")
