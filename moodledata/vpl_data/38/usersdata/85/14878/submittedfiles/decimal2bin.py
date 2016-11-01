# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('Digite o valor de n: '))

r=n%10
while n//10>0:
    a=r*(2**(n-1))
    