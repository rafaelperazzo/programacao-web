# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a:'))
b=1
soma=0
if  a<0:
    a=a*(-1)
while a-b>0:
    if b/(a-(b-1))<=0:
        soma=soma+(b/(a-(b-1))):
    b=b+1
  
print(soma)