# -*- coding: utf-8 -*-
from __future__ import division

b=input('Digite o valor de b:')
cont=2

while b//10!=1:
    cont=cont+1
    b=b//10
    n=cont
    
k=0
m=0    
while k<=n-1:
    (b%10)*2**k
    b=b//10
    k=k+1
    m=m+(b%10)*2**k
print m
prin n