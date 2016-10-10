# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n:')
x=1
cont=0

for i in range (0,n+1,1):
    if x%2==0:
        x=(x*(-1))
    a=x//(x**2)
    cont=cont+a
    x=x+1
    print ('%.5f'%cont)