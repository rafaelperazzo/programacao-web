# -*- coding: utf-8 -*-
from __future__ import division

def pico(l):
    posicao = 0
    for i in range (0,len(l)-1,1):
        if (l[i]>l[i+1]):
            posicao = i
            break 
    
    cont = 0
    for i in range (posicao,len(l)-1,1):
        if (l[i]<=l[i+1]):
            cont = cont+1
        
    if (cont==0 and posicao!=0):
        return True
    else:
        return False

n = input ('Digite n:')
a = []

for i in range (0,n,1):
    a.append (input ('Digite um elemento da lista:'))

if pico(a):
    print ('S')
else:
    print ('N')
        

