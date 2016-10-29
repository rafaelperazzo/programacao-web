# -*- coding: utf-8 -*-
from __future__ import division

n=input ('Digite o valor de n:')

contador=0
i=n

while i>0:
    i=i//10
    contador=contador+1
a=contador
i=0
soma=0

while i<=(a-1):
    j=n%10
    n=n//10
    d=j*(2**i)
    d=soma+1
    i=i+1
    
print (soma)

