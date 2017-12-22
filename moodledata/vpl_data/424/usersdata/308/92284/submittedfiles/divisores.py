# -*- coding: utf-8 -*-
import math

multiplos = []
n = int(int(input('Insira n: '))/2)
a = int(input('Insira a: '))
b = int(input('Insira b: '))

for i in range(1, n):
    multiplos.append(i*a)
    
for i in range(1, n*2):
    if (i*b) in multiplos:
        continue
    multiplos.append(i*b)    
    
multiplos.sort()
for i in range(0, n*2):
    print(multiplos[i])
    
