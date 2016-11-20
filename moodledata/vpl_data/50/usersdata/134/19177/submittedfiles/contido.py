# -*- coding: utf-8 -*-
from __future__ import division

n = input('Quantidade de elementos de a:')
a = []
for i in range(0,n,1):
    a.append(input('Digite um valor:'))

m = input('Quantidade de elementos de b:')
b = []
for i in range(0,m,1):
    b.append(input('Digite um valor:'))
    
def lista(a):
    for i in range (0,len(a),1):
        a = a[i]
        return a[i]

print a


   