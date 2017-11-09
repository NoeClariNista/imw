# PROGRAMA 1.

from math import sqrt

import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if ((b**2 - 4*a*c) < 0):
    print("La Ecuación No Tiene Solución Real.")

else:
	
    if (a == 0):
        x = -c / b
        print ("El Resultado De La Ecuacion Es",x,".")
        
    else:
        x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
        x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
        print("Los Resultados De La Ecuacion Son:",x1,"Y",x2,".")

