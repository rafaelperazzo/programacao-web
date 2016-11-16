# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite n:')
l = []

for i in range (0,n,1):
    l.append (input ('Digite um elemento da lista:'))

posicao = 0
for i in range (0,len(l)-2,1):
    if (l[i]>l[i+1]):
        posicao = i
        break 

for i in range (posicao,len(l)-2,1):
    if (l[posicao]<l[i+1]):
        print ('S')
    print ('N')
    
        

