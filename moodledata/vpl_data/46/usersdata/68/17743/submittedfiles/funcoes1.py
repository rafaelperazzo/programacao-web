# -*- coding: utf-8 -*-
from __future__ import division

#def crescente (a):
n=input('Digite n:')
a=[]
cont=0
for i in range (0,n,1):
    a.append (input('Digite um elemento da lista:'))
    
for i in range (0, len(a)-1,1):
    if a[i]>a[i+1]:
        cont=cont+1