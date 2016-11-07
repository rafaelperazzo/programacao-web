# -*- coding: utf-8 -*-
from __future__ import division
def lecker (lista):
    contador = 0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                contador = contador+1
        elif i == (len(lista)-1):
            if lista[i]>lista[i-1]:
                contador = contador +1
        else:
            if lista[i]> lista[i+1] and lista[i]>lista[i-1]:
                contador = contador +1
    if contador ==1:
        return True
    else:
        return False
                
n = input ('Digite a quantidade de termos:')
a = []
b = []
for i in range (0,n,1):
    a.append (input('Digite um número para lista a:'))
for j in range (0,n,1):
    b.append (input('Digite um número para lista b:'))

if lecker(a):
    print ('S')
else:
    print ('N')
if lecker(b):
    print ('S')
else:
    print ('N')