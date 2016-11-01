# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite o valor de n:'))

i=0
j=n
cont=0

while i<j:
    j=j//10
    cont=cont+1
    
soma=0
b=n

while i<cont:
    c=b%10
    b=b//10
    
    soma=soma+(c*(2**i))
    
    i=i+1
    
print (soma)
