# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
i=1
contador=0
while contador<=n:
    x=a*i
    y=b*i
    if i==b:
        print(y)
        contador=contador+1
    else:
        print(x)
        print(y)
        contador=contador+2
    i=i+1
    
    
