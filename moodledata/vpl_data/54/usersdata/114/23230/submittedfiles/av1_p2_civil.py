# -*- coding: utf-8 -*-
from __future__ import division
import math

def maior (a):
    maior_el = a[0]
    for i in range (0,len(a),1):
        if a[i] > maior_el:
            maior_el = a[i]
    return a[i]        
def menor (a):
    menor_el = a[0]
    for i in range (0,len(a),1):
        if a[i] < menor_el:
            menor_el = a[i]
    return menor_el
def quant_minima (a,m):
    soma =(math.fabs( maior(a) - m )) + (math.fabs( menor (a) - m ) )
    return soma
    
n = int(input('digite a quantidade de elementos da lista: '))
m = int(input('digite a altura: '))

a = []
for i in range (0,n,1):
    a.append (int(input('digite os elementos da lista: ')))

x = quant_minima (a,m)
print ('%d' %x)