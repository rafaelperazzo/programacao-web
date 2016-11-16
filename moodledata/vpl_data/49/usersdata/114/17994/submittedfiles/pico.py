# -*- coding: utf-8 -*-
from __future__ import division

def pico(l):
    posiçao=0
    for i in range(0,len(l)-1,1):
        if l[i] > l[i+1]:
            posiçao = i
            break
cont = 0
for i in range(posiçao,len(l)-1,1):
    if l[i]<=l[i+1]:
        cont = cont + 1
if cont == 0 and posiçao != 0:
    return True
else:
    return False
   
n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range(0,n,1):
    a.append(input('Digite os elementos da lista: '))

if pico(a):
    print ('S')
else:
    print ('N')

