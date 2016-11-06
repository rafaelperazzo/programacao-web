# -*- coding: utf-8 -*-
from __future__ import division

b=input('Digite número binário: ')
cont=0
n=b
while n>=1:
    cont=cont+1
    n=n//10
i=0
s=0
while b>0:
    r=b%10
    s=r*2**i
    i=i+1
print(s)
        
    