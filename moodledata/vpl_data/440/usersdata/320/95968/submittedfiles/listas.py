# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de termos: '))
lista = []
degrau = 0
for i in range (0, n, 1):
    lista.append(int(input('Digite: ')))
for i in range (0, n-1, 1):
    de = lista[i + 1] - lista[i]
    if de < 0:
        de = de*(-1)
    if de > degrau:
        degrau = de
print (degrau)

