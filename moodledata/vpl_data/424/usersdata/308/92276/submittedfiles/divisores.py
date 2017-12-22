# -*- coding: utf-8 -*-
import math

multiplos = []
n = int(int(input('Insira n: '))/2)+1
a = int(input('Insira a: '))
b = int(input('Insira b: '))

for i in range(1, n):
    multiplos.append(i*a)
    
for i in range(1, n):
    if (i*b) in multiplos:
        continue
        n = n+1
    multiplos.append(i*b)    
    
multiplos.sort()
print(multiplos)
