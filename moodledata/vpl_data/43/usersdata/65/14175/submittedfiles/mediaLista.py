# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n: ')

l=[]

for i in range(0,n,1):
    l.append(input('Digite um elemento: '))
    
print(l[0])
print(l[len(l)-1])

soma=0

for i in range(0,n,1):
    soma=(soma+l[i])
    
media=((soma)/(len(l)))

print(l)
    
