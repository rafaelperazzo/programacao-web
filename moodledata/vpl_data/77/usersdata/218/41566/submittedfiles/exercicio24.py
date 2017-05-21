# -*- coding: utf-8 -*-
import math
a=int(input('digite o valor de a:'))
b=int(input('digite o valor de b:'))
if a<=b:
    i=a
else:
    i=b
contador=0
while contador=0:
    if (a%i)==0 and (b%i)==(a%i):
        contador=1
    else:
        i=i-1
print(i)        