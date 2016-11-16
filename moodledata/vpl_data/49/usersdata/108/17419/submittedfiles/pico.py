# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    posicaomax=0
    for i in range (0,len(lista)-1,1):
        if (l[i]>l[i+1]):
            posicaomax = i
            break 
        
    contador=0
    for i in ange (posicaomax,len(l),1):
        if (l[i]>l[i+1]):
            contador = contador +1
    
    if (contador==0 and posicaomax!=0):
        return True 
    
    if (contador>0):
        return False
        

n = input('Digite a quantidade de elementos da lista: ')
l = []

for i in range (0,n,1):
    l.append ( input ('Digite um elemento:'))
    
if (pico):
    print ('S')
else:
    print ('N')


