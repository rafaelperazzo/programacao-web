# -*- coding: utf-8 -*-
n = int(input('digite: '))
lista = []
degrau = 0

for i in range(0,n,1):
    lista.append(int(input('digite: ')))

for i in range (0,n-1,1):
    dg = lista[i+1] - lista[i]
    if dg<0:
        dg = dg*(-1)
    if dg>degrau:
        degrau = dg
print (degrau)
