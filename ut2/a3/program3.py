# PROGRAMA 3.

import sys

numero1 = int(sys.argv[1])
numero2 = int(sys.argv[2])

if (numero1 <= 0 or numero2 <= 0):
    print("Error.")
else:
    if (numero1 < numero2):
        for i in range(numero1, 0, -1):
            if (numero1 % i == 0 and numero2 % i == 0):
                print ("El MCD De", numero1, "Y", numero2, "Es", i)
                break
    elif (numero1 == numero2):
        print("El MCD De", numero1, "Y", numero2, "Es", numero1)
    else:
        for i in range(numero2, 0, -1):
            if (numero2 % i == 0 and numero1 % i == 0):
                print ("El MCD De", numero1, "Y", numero2, "Es", i)
                break
