# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input('Digite o valor de n:')
i=1
j=n-1

while n>=i:
    if j%2==0:
        a=1/(i*(3**j))
        
    else:
        a=-(1/(i*(3**j)))
    
    i=i+2
    j=j+1
    a=a+1
pi=(12**(1/2))*(a+1)

print ('%.6f'%pi)