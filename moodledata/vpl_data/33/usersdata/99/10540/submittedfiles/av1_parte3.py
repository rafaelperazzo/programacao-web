# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO
n=input('Digite o valor de n:')
i=1
j=n-1

while i<=n:
    if j%2==0:
        a=(1/(i*(3**j)))
        
    else:
        a=-(1/(i*(3**j)))
    
    pi=(12**0.5)*a
        
    i=i+2
    a=a+1
    
print ('%.6'%pi)