# -*- coding: utf-8 -*-
from __future__ import division

a= int(input('Digite o valor de a:'))
b= int(input('Digite o valor de b:'))
c= int(input('Digite o valor de c:'))

contadorA=0
contadorB=0

if c%a==0:
    contadorA=contadorA+1
else:
    print('N')
    
    if c%b==0:
        contadorB=contadorB+1
    else:
        print ('N')
    
