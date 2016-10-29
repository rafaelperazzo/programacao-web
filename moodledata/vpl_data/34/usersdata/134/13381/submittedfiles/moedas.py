# -*- coding: utf-8 -*-
from __future__ import division
a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))
c = int(input('Digite o valor de c:'))

R1 = c//a
resto1 = c%a
R2 = resto1//b
resto2 = resto1%b

if resto1 != 0:
    if resto2 != 0:
        R3 = c//b
        if c%b==0:
            print ('0')
            print ('%d' %R3)
        else:
            print ('N')
    if resto2 == 0:
        print ('%d' %R1)
        print ('%d' %R2)
        
        
if resto1 == 0:
    print ('%d' %R1)
    print ('0')


