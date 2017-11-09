# PROGRAMA 3.

import sys

nota = float(sys.argv[1])

if (0 <= nota < 5):
    print("Suspenso.")
    
elif (5 <= nota < 7):
    print("Aprobado.")
    
elif (7 <= nota < 9):
    print ("Notable.")
    
elif (9 <= nota < 10):
    print ("Sobresaliente.")
    
elif (10 == nota):
    print ("Matricula De Honor.")
    
else:
    print ("Error.")
