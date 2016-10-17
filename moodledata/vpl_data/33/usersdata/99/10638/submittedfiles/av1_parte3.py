# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input('Digite o valor de n:')
i=1
j=n-1
soma=0

while n>=(i-1):
    if j%2==0:
        a=1/(i*(3**j))
        
    else:
        a=-(1/(i*(3**j)))
        
    soma=soma+a
    i=i+2
    j=j+1
    
pi=(12**0.5)*(soma)
print ('%.6f'%pi)