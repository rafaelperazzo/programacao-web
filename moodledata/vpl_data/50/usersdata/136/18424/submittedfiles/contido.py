# -*- coding: utf-8 -*-
from __future__ import division

#FUNCAO
def contido(x,y):
    cont = 0
    for i in range (0, len(y), 1):
        if y[i] in x:
            cont = cont + 1
    return cont

#PROGRAMA PRINCIPAL
n = input("Digite n:")
m = input("Digite m:")

a = []
for i in range(0,n,1):
    a.append(input("Digite um elemento:"))
b = []
for i in range(0,m,1):
    b.append(input("Digite um elemento:"))

#SAIDA
print contido(a,b)

