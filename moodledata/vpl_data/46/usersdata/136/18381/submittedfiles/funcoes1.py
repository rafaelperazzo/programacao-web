# -*- coding: utf-8 -*-
from __future__ import division
def crescente (lista):
    cont = 0
    for i in range (0,len(lista),1):
        if i == 0:
            if lista[0] < lista[1]:
                cont = cont + 1
        elif i == (len(lista) - 1):
            if lista[len(lista)-1] > lista[len(lista)-2]:
                cont = cont +1
        else:
            if lista[i] > lista[i-1] and lista[i]<lista[i+1]:
                cont = cont +1
    if cont == (len(lista)):
        return True
    else:
        return False

def decrescente (lista):
    cont = 0
    for i in range (0,len(lista),1):
        if i == 0:
            if lista[0] > lista[1]:
                cont = cont + 1
        elif i == (len(lista) - 1):
            if lista[len(lista)-1] < lista[len(lista)-2]:
                cont = cont +1
        else:
            if lista[i] < lista[i-1] and lista[i]>lista[i+1]:
                cont = cont +1
    if cont == (len(lista)):
        return True
    else:
        return False

def igualdade (lista):
    cont = 0
    for i in range (0,len(lista),1):
        if i == 0:
            if lista[0] == lista[1]:
                cont = cont + 1
        elif i == (len(lista) - 1):
            if lista[len(lista)-1] == lista[len(lista)-2]:
                cont = cont +1
        else:
            if lista[i] == lista[i-1]:
                cont = cont +1
    if cont > 0:
        return True
    else:
        return False
n = input("Digite n:")
a = []
b = []
c = []

for i in range (0, n, 1):
    a.append(input("Digite um elemento:"))
for i in range (0, n, 1):
    b.append(input("Digite um elemento:"))
for i in range (0, n, 1):
    c.append(input("Digite um elemento:"))
print def crescente (a)
print def crescente (b)
print def crescente (c)
print def decrescente (a)
print def decrescente (b)
print def decrescente (c)
print def igualdade (a)
print def igualdade (b)
print def igualdade (c)