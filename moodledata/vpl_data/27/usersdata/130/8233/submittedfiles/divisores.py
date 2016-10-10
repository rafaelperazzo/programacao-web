# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
contador=0
while True:
    if a==b:
        print(b)
        contador=contador+1
    else:
        print(a)
        print(b)
        contador=contador+2
    a=a+a
    b=b+b
    if contador==n:
        break