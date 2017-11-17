# PROGRAMA 2.
import sys
numero = int(sys.argv[1])
if (numero <= 0):
    print("Error.")
else:
    suma = 0
    for i in range(1, numero + 1):
        suma += i**2
    print("El Resultado Final Es", suma)
