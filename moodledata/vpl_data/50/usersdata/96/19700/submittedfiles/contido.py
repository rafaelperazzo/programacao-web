# -*- coding: utf-8 -*-
from __future__ import division

def conido(a,b):
    contador = 0
    for i in range(0, len(a),1):
        if a[i] in b:
            contador = contador + 1
    return contador

n = input('Digite o valor de n:')
m = input('Digite o valor de m:')
a = []
b = []

for i in range(0,n,1):
    a.append(input('Digite um valor:')
for i in range(0,m,1):
    b.append(input('Digite um valor:')
    
print contido(a,b)