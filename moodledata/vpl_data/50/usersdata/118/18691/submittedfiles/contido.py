# -*- coding: utf-8 -*-
from __future__ import division

def contido(a,b):
    cont = 0
    for i in range(0,len(b),1):
        if b[i] in a:
            cont = cont +1
    return cont
    
n = input('Digite o número de termos da primeira lista:')
m = input('Digite o número de termos da segunda lista:')
a = []
b = []

for i in range(0,n,1):
    a.append(input('Digite um valor para a primeira lista:'))
for i in range(0,m,1):
    b.append(input('Digite um valor para a segunda lista:'))

print('%.d' %contido(a,b))