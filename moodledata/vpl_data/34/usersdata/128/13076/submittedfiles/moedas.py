# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite o valor de uma moeda: ')
b=input('Digite o valor de outra moeda: ')
c=input('Digite o valor da cédula: ')

aA=a
bB=b

a2=0
b2=0

contA=0
contB=0

while True:
    a2=a2+aA
    contA=contA+1
    
    b2=b2+bB
    contB=contB+1
    
    if (c-a2)%b==0:
        qb=(c-a2)/b
        print contA
        print ('%.d' %qb)
        break
    
    if (c-b2)%a==0:
        qa=(c-b2)/a
        print ('%.d' %qa)
        print contB
        break
    
    if a2>c or b2>c:
        print ('N')
        break