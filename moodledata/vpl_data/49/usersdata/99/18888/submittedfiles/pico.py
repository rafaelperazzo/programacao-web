# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1] and lista[i]>lista[i-1]:
            cont=cont+1
    
    if cont==1:
        return True
    else:
        return False


n = input('Digite a quantidade de elementos da lista: ')
a=[]

for i in range(0,n,1):
    a.append(input('Digite um valor de a:'))
    
if pico(a):
    print("S")
else:
    print("N")
    
