# -*- coding: utf-8 -*-
from __future__ import division

def elementos_contidos (x,y):
    cont=0
    for i in range (0,len(y),1):
        if y[i] in x:
            cont = cont + 1
    return cont        

n = input('digite a quantidade n de elementos: ')
m = input('digite a quantidade m de elementos: ')
a = []
b = []

for i in range (0,n,1):
    a.append(input('digite os elementos da lista a: '))
    
for i in range (0,m,1):
    b.append(input('digite os elementos da lista b: '))
    
print elementos_contidos (a,b)
    