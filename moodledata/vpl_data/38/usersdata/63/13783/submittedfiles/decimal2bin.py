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
 while m<=(j-1):
     r=a%10
     a=a//10
     d=r*(2**l)
     soma+=d
     m=m+1
print (soma)