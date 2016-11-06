# -*- coding: utf-8 -*-
from __future__ import division

n= input ('Digite o valor de n:')
a=[]
pares=impares=0
qpares=qimpares=0

for i in range (0,n,1):
    a.append (input ('Digite o valor do elemento:'))

for j in range (0,n,1):
    if a[j]%2==0:
       pares=pares+a[j]
       qpares=qpares+1
    else:
        impares=impares+a[]
        qimpares=qimpares+1

print impares
print pares
print qimpares
print qpares
print (a)