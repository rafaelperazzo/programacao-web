# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidades de termos:')
a=[]
soma=0
so=0
cont=0
co=0

for i in range (1,n+1,1):
    a.append(input('digite um valor da lista'))
    if sum(a)%2==1:
        soma=soma+sum(a)
        cont=cont+1
    if sum(a)%2==0:
        so=so+sum(a)
        co=co+1
        
print soma
print so
print cont
print co
print a
    
        