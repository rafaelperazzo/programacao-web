# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de n:'))
b=1
soma=0
if  a<0:
    a=a*(-1)
while b/(a)>-1:
    soma=soma+(b/(a))
    b=b+1
    
    
print(soma)