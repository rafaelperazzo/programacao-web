# -*- coding: utf-8 -*-
from __future__ import division

b=input('Insira um valor na base b:')
n=0
c=b
while c>0:
    n=n+1
    c=c//10
soma=0
i=0
while i<n:
    soma=soma+((b%10)*(2**i))
    b=b//10
    i=i+1
print(soma)