# PROGRAM 4.

import sys

numbers = sys.argv[1:]
quantity = len(numbers)
summ = 0

for i in range(0, quantity):
	summ += float(numbers[i])
half = summ / quantity
print("La Media De Los Valores Es:", half)
