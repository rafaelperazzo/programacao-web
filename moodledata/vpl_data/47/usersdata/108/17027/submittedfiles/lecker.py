# -*- coding: utf-8 -*-
from __future__ import division

def listalecker (lista):
    for i in range (0,len(lista),1):
        if (lista[i] > lista[i-1]) and lista[i] > lista [i+1]):
            contador = contador +1
    if (contador==1):
        return True
    else:
        return False
    
n = input ('Digite o tamanho da lista:')
a = []
b = []
    
for i in range (0,n,1):
    a.append (input ('Digite um elemento da lista a:'))
    
for i in range (0,n,1):
    b.append (input ('Digite um elemento da lista b:'))

if listalecker(a):
    print ('S')
else:
    print ('N')

if listalecker(b):
    print ('S')
else:
    print ('N')
        

