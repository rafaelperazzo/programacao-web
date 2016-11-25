# -*- coding: utf-8 -*-
from __future__ import division

def crescente(lista):
    i = 0
    cont = 0
    
    while (len(lista)-1)>i:
        if lista[i]<lista[i+1]:
            cont=cont+1
        i=i+1
    if (len(lista)-1)==cont:
        return True
    else:
        return False
def decrescente(lista1):
    j = 0
    cont1 = 0
    
    while (len(lista1)-1)>j:
        if lista1[j]>lista1[j+1]:
            cont1=cont1+1
        j=j+1
    if (len(lista1)-1)==cont1:
        return True
    else:
        return False
def ciguais(lista2):
    k = 0
    cont2 = 0
    
    while (len(lista2)-1)>k:
        if lista2[k]==lista2[k+1]:
            cont2 = cont2+1
        k=k+1
    if cont2>0:
        return True
    else:
        return False

n = input('Digite o tamanho do vetor: ')

x = 1
y = 1
z = 1

a = []
b = []
c = []

while n>=y:
    a.append(input('Digite os valores do vetor A: '))
    y=y+1
while n>=x:
    b.append(input('Digite os valores do vetor B: '))
    x=x+1
while n>=z:
    c.append(input('Digite os valores do vetor C: '))
    z=z+1

if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if ciguais(a):
    print('S')
else:
    print('N')
if crescente(b):
    print('S')
else:
    print('N')
if decrescente(b):
    print('S')
else:
    print('N')
if ciguais(b):
    print('S')
else:
    print('N')
if crescente(c):
    print('S')
else:
    print('N')
if decrescente(c):
    print('S')
else:
    print('N')
if ciguais(c):
    print('S')
else:
    print('N')
    

