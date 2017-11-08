# PROGRAMA 4.

from math import pi

import sys

r = float(sys.argv[1])

y = int(input("Opciones: \n(1) Calcular El Diámetro De La Circunferencia. \n(2) Calcular El Perímetro De La Circunferencia. \n(3) Calcular El Área Del Círculo. \n(4) Salir. \n"))

if (y==1):
    d = 2 * r
    print("El Diametro De La Circunferencia Es:",d)
elif (y==2):
    p = 2 * pi * r
    print("El Perimetro De La Circunferencia Es:",p)
elif (y==3):
    a = pi * r**2
    print("El Area Del Circulo Es:",a)
elif (y==4):
    print("Saliendo.")
else:
    print("Error.")
