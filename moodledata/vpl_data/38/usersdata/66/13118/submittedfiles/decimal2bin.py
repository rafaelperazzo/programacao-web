# -*- coding: utf-8 -*-
from __future__ import division
n=int(input("digite n:"))
a=n
cont=0
while n>0:
    n=n//10
    cont=cont+1
i=0
soma=0
while i<a:
    soma=soma+((a%10)*(2**i)
    i=i+1
    a=a//10
print soma
