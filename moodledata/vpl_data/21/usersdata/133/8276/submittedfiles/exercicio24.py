# -*- coding: utf-8 -*-
from __future__ import division
import math

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')

r=a%b
if r>0:
    a=b
    b=r
    r=a%b
print (r)