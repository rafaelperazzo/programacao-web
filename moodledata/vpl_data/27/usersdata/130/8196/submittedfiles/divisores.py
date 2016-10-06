# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
i=0
contador=0
while True:
    x=a*i
    y=b*i
    if i==a:
        print(x)
        contador=contador+1
    else:
        print(x)
        print(y)
        contador=contador+2
    i=i+1
    if contador==n:
        break
