# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite o valor de a:')
b=input('digite o valor de b:')
c=input('digite o valor de c:')
cont=0
quantidade_a=c//a
quantidade_b=0
while quantidade_a>=0:
    troco=c-quantidade_a*a
    if troco%b==0:
        quantidade_b=troco//b
        cont=cont+1
        break
    else:
        quantidade_a=quantidade_a-1
if cont>0:
    print(quantidade_a)
    print(quantidade_b)
else:
    print(não)