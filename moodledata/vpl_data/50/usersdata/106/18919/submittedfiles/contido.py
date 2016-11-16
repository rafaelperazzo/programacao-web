# -*- coding: utf-8 -*-
from __future__ import division

def quantidade (lista1, lista2):
    contador = 0
    for i in range (0,len(lista2),1):
        if lista2[i] in lista1:
            contador = contador +1
    return contador
    
n = input ('Digite a quantidade de termos de a:')
m = input ('Digite a quantidade de termos de b:')
a = []
b = []
for i in range (0,n,1):
    a.append (input('Digite um valor:'))
    
for i in range (0,m,1):
    b.append (input ('Digite um valor:'))

print (quantidade(a,b))