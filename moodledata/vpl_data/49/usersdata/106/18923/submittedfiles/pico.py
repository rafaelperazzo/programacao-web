# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    indice=0
    for i in range (0,len(lista)-1,1):
        if a[i]==a[i+1]:
            return False
            break
        elif a[i]>a[i+1]:
            indice = i
            break
    for i in range (indice,len(lista)-1,1):
        if a[i]<=a[i+1] or indice==0:
            return False
        else:
            return True
    


n = input('Digite a quantidade de elementos da lista: ')
a = []
for i in range (0,n,1):
    a.append (input('Digite um valor para a lista:')
if pico(a):
    print ('S')
else:
    print ('N')
