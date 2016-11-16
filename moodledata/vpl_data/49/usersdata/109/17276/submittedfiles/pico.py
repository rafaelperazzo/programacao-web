# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    cont=0
    cont2=0
    i=0
    while True:
        if lista[i+1]>lista[i]:
            cont=cont+1
            i=i+1
        if lista[i+1]<lista[i]:
            break
    if cont==n-1:
        cont2=
    for i in range (cont,n-1,1):
        if lista[i+1]>lista[i]:
            cont2=cont2+1
            
    if cont==0:
        return False       
    if cont2==0:
        return True
    if cont2!=0:
        return False
    

n = input('Digite a quantidade de elementos da lista: ')
a=[]
for i in range (0,n,1):
    a.append(input('Digite um elemento da lista:'))
    
if pico(a):
    print 'S'
else:
    print 'N'
    
