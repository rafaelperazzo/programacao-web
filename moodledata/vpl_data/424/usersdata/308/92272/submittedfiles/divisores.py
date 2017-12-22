# -*- coding: utf-8 -*-
import math

multiplos = []
n = int(input('Insira n: '))
a = int(input('Insira a: '))
b = int(input('Insira b: '))

for i in range(1, int((n+1)/2)+1):
    multiplos.append(i*a)
    
for i in range(1, int((n+1)/2)+1):
    multiplos.append(i*b)    
    
multiplos.sort()
print(multiplos)
