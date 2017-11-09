# PROGRAMA 2.

from math import sqrt

import sys

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])
x3 = float(sys.argv[5])
y3 = float(sys.argv[6])

d2 = sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
d3 = sqrt(((x1 - x3)**2) + ((y1 - y3)**2))

if (d2 < d3):
    print ("El Punto Más Cercano A (",x1,",",y1,") Es (",x2,",",y2,") Y Está A Una Distancia De",d2)

elif (d2 > d3):
    print ("El Punto Más cercano A (",x1,",",y1,") Es (",x3,",",y3,") Y Está A Una Distancia De",d3)

else:
    print("La Distancia Entre El Punto (",x1,",",y1,") Y (",x2,",",y2,") Es La Misma Distancia Entre El Punto (",x1,",",y1,") Y (",x3,",",y3,") Y Esa Distancia Es",d2)
