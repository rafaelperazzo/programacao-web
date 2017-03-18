# -*- coding: utf-8 -*-
from __future__ import division

b= input('Digite o valor de b: ')
n= input('Digite o valor de n: ')

r= b%10
soma=0
for i in range(0,n,1):
    soma= soma+(r*(2**i))
    b= b//10
    r= b%10
    
print soma