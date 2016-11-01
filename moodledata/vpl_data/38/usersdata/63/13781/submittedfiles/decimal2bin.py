# -*- coding: utf-8 -*-
from __future__ import division

a=input('digite um numero:')
i=b
contador=0

while i>0:
    i=i//10
    contador+=1
j=contador
l=0
somatorio=0
 while l<=(j-1):
     r=a%10
     a=a//10
     d=r*(2**l)
     somatorio+=d
     l=l+1
print (somatorio)