# -*- coding: utf-8 -*-
from __future__ import division
def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
            cont=cont+1
    if cont==1:
        return True
    else:
        return False
def teste(lista):
    if lecker(lista):
        return print('S')
    else:
        return print('N)
n=input('Digite o valor de n:')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('Digite um valor para a:'))
for i in range(0,n,1):
    b.append(input('Digite um valor para b:'))

print(teste(a))
print(teste(b))