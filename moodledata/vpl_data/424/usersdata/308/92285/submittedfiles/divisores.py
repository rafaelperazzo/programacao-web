# -*- coding: utf-8 -*-
import math

multiplos = []/2)
a = int(input('Insira a: '))
b = int(input('Insira b: '))

for i in range(1, n):
    multiplos.append(i*a)
    
for i in range(1, n):
    if (i*b) in multiplos:
        continue
    multiplos.append(i*b)    
    
multiplos.sort()
for i in range(0, n):
    print(multiplos[i])
    
