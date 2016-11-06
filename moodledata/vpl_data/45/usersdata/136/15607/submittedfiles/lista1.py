# -*- coding: utf-8 -*-
from __future__ import division

n = input("Digite n:")
a = []

for i in range (0, n, 1):
    a.append(input("Digite um valor:"))

soma = 0
somab = 0
contador = 0
contadorb = 0
for i in range (0, n, 1):
    if a[i]%2!=0:
        soma = soma + a[i]
        contador = contador + 1
    else:
        somab = somab + a[i]
        contadorb = contadorb + 1

print soma
print somab
print contador
print contadorb
print a