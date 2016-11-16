# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    cont=0
    i=0
    while True:
        lista[i+1]>lista[i]:
            cont=cont+1
            i=i+1
            break
    for i in range (cont,n,1):
        if lista[i+1]<lista[i]:
            return True
        else: 
            return False
    

n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range (0,n,1):
    a.append(input('Digite um elemento da lista:'))
    
if pico(a):
    print 'S'
else:
    print 'N'
    
