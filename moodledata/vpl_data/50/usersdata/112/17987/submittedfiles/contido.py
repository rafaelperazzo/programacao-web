# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de elementos da lista A:')
m=input('Digite a quantidade de elementos da lista B:')
a=[]
b=[]
for i in range (0,n,1):
    a.append(input('Digite o elemento da lista A:'))
for i in range (0,m,1):
    b.append(input('Digite o elemento da lista B:'))
cont=0
for i in range (0,len(a),1):
    for i in range (0,len(b),1):
        if a[i]==b[i]:
            cont=cont+1
            if cont>0:
                print 'S'
