# VARIABLES.

import sys
dinero = sys.argv[1]
dinero = int(dinero)

print ("\nLa Cantidad De Billetes / Monedas Para Obtener ",dinero," Es:")

# BILLETES DE 50 €.

dinero_50_resto = dinero % 50
dinero_50_billetes = dinero // 50

if (dinero_50_billetes != 0):
    print ("\n*",dinero_50_billetes,"Billete(s) De 50 €.\n")

# BILLETES DE 20 €.

dinero_20_resto = dinero_50_resto % 20
dinero_20_billetes = dinero_50_resto // 20

if (dinero_20_billetes != 0):
    print ("\n*",dinero_20_billetes,"Billete(s) De 20 €.\n")

# BILLETES DE 10 €.

dinero_10_resto = dinero_20_resto % 10
dinero_10_billetes = dinero_20_resto // 10

if (dinero_10_billetes != 0):
    print ("\n*",dinero_10_billetes,"Billete(s) De 10 €.\n")

# BILLETES DE 5 €.

dinero_5_resto = dinero_10_resto % 5
dinero_5_billetes = dinero_10_resto // 5

if (dinero_5_billetes != 0):
    print ("\n*",dinero_5_billetes,"Billete(s) De 5 €.\n")

# MONEDAS DE 2 €.

dinero_2_resto = dinero_5_resto % 2
dinero_2_monedas = dinero_5_resto // 2

if (dinero_2_monedas != 0):
    print ("\n*",dinero_2_monedas,"Moneda(s) De 2 €.\n")

# MONEDAS DE 1 €.

dinero_1_resto = dinero_2_resto % 1
dinero_1_monedas = dinero_2_resto // 1

if (dinero_1_monedas != 0):
    print ("\n*",dinero_1_monedas,"Moneda(s) De 1 €.\n")
