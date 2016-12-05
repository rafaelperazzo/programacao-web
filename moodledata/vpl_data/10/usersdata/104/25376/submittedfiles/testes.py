# -*- coding: utf-8 -*-
from __future__ import division
def modulo(x):
    if x>=0:
        return (x)
    else:
        return (-x)
def fatorial(x):
    f=1
    for i in range(1,x+1,1):
        f=f*i
    return f

z=input('Digite um valor z:')
epsilon=input('Digite um epsilon
cos_z=1
cont=0
e=fatorial(i)
f=z**i
t=z/e
while t>=0:
    if cont==0:
        cos_z=cos_z-t
        cont=1
    else:
        cos_z=cos_z+t

print ('%.15f'%(cos_z))
        
    
