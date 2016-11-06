# -*- coding: utf-8 -*-
from __future__ import division

b=input('Digite o valor de b:')
cont=2
m=0

while b//10!=1:
    cont=cont+1
    b=b//10
    n=cont
    
for i in range (0,n,1):
    (i*2**n-1)=m
    n-1=(n-1)-1
print m