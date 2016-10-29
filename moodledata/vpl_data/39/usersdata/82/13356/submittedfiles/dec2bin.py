# -*- coding: utf-8 -*-
from __future__ import division

n= input ('Digoite o valor de n:')

contador=0
i=n

while i>0:
    i=i//2
    contador+=1
a=contador
soma=0
k=0
while k<=(a-1):
    r=n%2
    n=n//2
    b=r*(10**k)
    k+=1
    soma=soma+b
print (soma)