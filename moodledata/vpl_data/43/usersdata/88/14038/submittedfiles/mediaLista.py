# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de elementos: ')
l=[]

for i in range (0,n,1):
    l.append(input('Digite o valor do elemento: '))
print (l[0])
print (l[n])

soma=0
for i in range (0,n,1):
    soma=(soma+l[i])/n
    print soma
    






