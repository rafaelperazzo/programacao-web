# -*- coding: utf-8 -*-
from __future__ import division

#FUNCAO
def contido(a,b):
    cont=0
    for i in range(0,len(b),1):
        if b[i] in a:
            cont = cont + 1
    return cont
#PROGRAMA
n = input('Quantidade de elementos de a:')
m = input('Quantidade de elementos de b:')

a = []
for i in range(0,n,1):
    a.append(input('Digite um valor:'))

b = []
for i in range(0,m,1):
    b.append(input('Digite um valor:'))

print contido(a,b)
    

        




   