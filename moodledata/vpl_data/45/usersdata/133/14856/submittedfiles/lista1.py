# -*- coding: utf-8 -*-
from __future__ import division

n= input('Digite o valor de n: ')
a=[]

for i in range(0,n,1):
    a.append(input('Digite o valor do número: '))
si=0
for i in range(0,n,1):
    if a[i]%2!=0:
        si=si+a[i]
sp=0
for i in range(0,n,1):
    if a[i]%2==0:
        sp=sp+a[i]
qi=0
for i in range(0,n,1):
    if a[i]%2!=0:
        qi=qi+1
qp=0
for i in  range(0,n,1):
    if a[i]%2==0:
        qp=qp+1
print si
print sp
print qi
print qp
print a