# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o número de termos:')

a = []
for i in range(0,n,1):
    a.append(input('Digite o valor:'))

somap = 0
somai = 0
contp = 0
conti = 0

for j in range(0,len(a),1):
    if a[j]%2 == 0:
        contp = contp +1
        somap = somap +a[j]
    else:
        conti = conti +1
        somai = somai +a[j]

print(somai)
print(somap)
print(conti)
print(contp)
print(a)