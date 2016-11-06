# -*- coding: utf-8 -*-
from __future__ import division

b=int(input('b:'))
x=b
cont=0
while x>0:
    x=x/10
    cont=cont+1
soma=0
for i in range(0,cont,1):
    j=b%10
    soma=soma+j*(2**i)
    b=b//10
print(soma)