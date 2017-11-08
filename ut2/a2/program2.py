# PROGRAMA 2.

from math import sqrt

import sys

x_1 = float(sys.argv[1])
y_1 = float(sys.argv[2])
x_2 = float(sys.argv[3])
y_2 = float(sys.argv[4])
x_3 = float(sys.argv[5])
y_3 = float(sys.argv[6])

d_2 = sqrt(((x_1-x_2)**2)+((y_1-y_2)**2))
d_3 = sqrt(((x_1-x_3)**2)+((y_1-y_3)**2))

if (d_2 < d_3):
    print ("El punto más cerca a (",x_1,",",y_1,") Es (",x_2,",",y_2,") y está a una distancia de",d_2)
elif (d_2 > d_3):
    print ("El punto más cerca a (",x_1,",",y_1,") Es (",x_3,",",y_3,") y está a una distancia de",d_3)
else:
    print("La distancia es la misma.")
