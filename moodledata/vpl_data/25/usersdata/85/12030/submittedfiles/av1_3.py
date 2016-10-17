# -*- coding: utf-8 -*-
from __future__ import division
import math

a= int(input('Digite o valor de a: '))
b= int(input('Digite o valor de b: '))

q=a
d=b
r=q%d
cont=1
if r==0:
    mdc=d
else:
    while r>0:
            cont=cont+1
            q=d
            d=r
            r=q%d
            mdc=d
print mdc
print cont
