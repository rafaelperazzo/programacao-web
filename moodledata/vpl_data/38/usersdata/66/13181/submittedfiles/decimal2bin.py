# -*- coding: utf-8 -*-
from __future__ import division
n=int(input("digite n:"))
i=0
soma=0
a=n
cont=0
while n>0:
    n=n//10
    cont=cont+1
print cont

while i<a:
    soma=soma+((a%10)*(2**i))
    a=a//10
    i=i+1
    
print soma
