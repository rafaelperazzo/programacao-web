# -*- coding: utf-8 -*-
from __future__ import division

b=input("Digite o N.: ")

soma=0
ib=1
n=0

whileb//ib!=0:
    n=n+1
    ib=ib*10
    
for i in range (0,n,1):
    d=(b%10)*(2**i)
    soma=soma+d
    b=b//10

print soma