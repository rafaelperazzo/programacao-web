# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite o valor de n:')
l=[]
for i in range (0,n,1):
    l.append(input('Digite um elemento:')

somati=0
somap=0
qnti=0
qntp=0

for i in range (0,l,1):
    if i//2==0:
        qntp=qntp+1
    elif i//2!=0:
        qnti=qnti+1

print qntp
print qnti