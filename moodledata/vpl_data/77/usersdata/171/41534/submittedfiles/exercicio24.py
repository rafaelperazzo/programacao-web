# -*- coding: utf-8 -*-
import math
n1=int(input('digite o valor n1:'))
n2=int(input('digite o valor n2:'))
contador=1
for i in range(1,n1,1):
    if n1 %i==0:
        contador=contador+1
    if n2%i==0:
        contador=contador-1
print(contador)
