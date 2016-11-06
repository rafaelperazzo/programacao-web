# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o número de termos:')

a = []
for i in range(0,n+1,1):
    a.append(input('Digite o valor:')

somaP = 0
somaI = 0
contP = 0
contI = 0

for j in range(0,len(a),1):
    if a[i]%2 == 0:
        contP = contP +1
        somaP = somaP +1
    else:
        contI = contI +1
        somaI = somaI +1

print(somaI)
print(somaP)
print(contI)
print(contP)
print(a)