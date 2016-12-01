# -*- coding: utf-8 -*-
from __future__ import division

def vida(a,b,c):
    cont=0
    for i in range(b,c+1,1):
        cont=cont+a[i]
    return cont
    
p=input('a quantidade de sala:')
b=input('porta de entrada:')
c=input('porta de saida:')
a=[]
for i in range(0,p,1):
    a.append(input('a quantidade de vida da sala:'))
print ('%d' %vida(a,b,c))