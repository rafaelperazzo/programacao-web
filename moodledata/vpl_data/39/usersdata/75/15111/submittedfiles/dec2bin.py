# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite o valor de n:'))

i=0
j=n
cont=0

while i<j:
    j=j//2
    cont=cont+1
    
soma=0
b=n

while i<cont:
    c=b%2
    b=b//2
    soma=soma+(c*(10**i))
    i=i+1
    
print (soma)

    

