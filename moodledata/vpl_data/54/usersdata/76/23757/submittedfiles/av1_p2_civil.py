# -*- coding: utf-8 -*-
from __future__ import division

p = input('Digite o numero de pinos:')
a = input('Digite a altura dos pinos:')

i = 1
v = []

while i<=p:
    v.append(input('Digite o tamanho dos pinos:'))
    i = i+1
    
    
j = 0
cont = 0

while j<(n-1):
    while v[j]>a and v[j+1]>a:
        v[j] = v[j]-1
        v[j]+1 = v[j+1]-1
        cont = cont + 1
    while v[j]<a and v[j+1]<a:
        v[j] = v[j]+1
        v[j+1] = v[j+1]+1
        cont = cont + 1
    while v[j]>a:
        v[j] = v[j]-1
        cont = cont + 1
    while v[j]<a:
        v[j] = v[j]+1
        cont = cont + 1
    j = j+1

if v[j]!=a:
    while v[j]>a:
        v[j] = v[j]-1
        cont = cont + 1
    while v[j]<a:
        v[j] = v[j]+1
        cont = cont + 1
        
print cont
print lista