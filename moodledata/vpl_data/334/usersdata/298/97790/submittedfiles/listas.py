# -*- coding: utf-8 -*-
import sort

def modulo(h):
    if h<0:
        h=(-1)*h
    return h

n = int(input('Digite a quantidade de elementos da lista: '))
while n<2:
    n = int(input('Digite a quantidade de elementos da lista: '))

lista=[]
for i in range (0, n, 1):
    lista.append(int(input('Digite um elemento para a lista: ')))

k=[]
for i in range (0, n-1, 1):
   d=lista[i] - lista[i+1]
   k.append(modulo(d))

print(k)
k.sort
print(k)