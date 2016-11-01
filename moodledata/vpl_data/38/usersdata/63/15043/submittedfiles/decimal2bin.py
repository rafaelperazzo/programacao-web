# -*- coding: utf-8 -*-
from __future__ import division

a=input('digite um numero:')
i=b
contador=0

while i>0:
    i=i//10
    contador+=1
j=contador

m=0
soma=0
n=a
 while m<=(j-1):
     n=a%2
     a=a//2
     b=n*(10**m)
     soma=soma
     m+=1
print (soma)