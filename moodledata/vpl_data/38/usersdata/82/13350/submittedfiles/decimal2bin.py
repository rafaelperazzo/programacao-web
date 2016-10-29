# -*- coding: utf-8 -*-
from __future__ import division

n=input ('Digite o valor de n:')

contador=0
i=n

while i>0:
    i=i//10
    contador=contador+1
a=contador
k=0
soma=0

while k<=(a-1):
    j=n%10
    n=n//10
    d=j*(2**k)
    d=soma
    k=k+1
    
print (soma)

