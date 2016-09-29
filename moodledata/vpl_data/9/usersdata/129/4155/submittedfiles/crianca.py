# -*- coding: utf-8 -*-
from __future__ import division
P1=input('Digite o valor de P1: ')
C1=input('Digite o valor de C1: ')
P2=input('Digite o valor de P2: ')
C2=input('Digite o valor de C2: ')
A=P1*C1
B=P2*C2
if A==B:
    print ('0')
elif A>B:
    print ('-1')
else :
    print ('1')
