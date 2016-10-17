# -*- coding: utf-8 -*-
from __future__ import division

#COMECE AQUI ABAIXO

n=input('digite um valor:')

soma=0
a=1
b=0

while 1<n:
    if b%2==0:
        soma=soma+(1/(a*(3**b)))
       
    else:
        soma=soma-(1/(a*(3**b)))
       
    a=a+2
    b=b+1
    pi=(12**0,5)*soma
    print('%.6f'%pi)