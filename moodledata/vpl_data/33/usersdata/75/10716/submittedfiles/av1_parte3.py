# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite o valor de n:')

i=0
j=1
soma=0

while i<=n:
    if i%2==0:
        soma=1/(j*(3**i))
    else:
        soma=-1/(j*(3**i))
    i=i+1
    j=j+2
print ('%.6f'%soma) 
        
    