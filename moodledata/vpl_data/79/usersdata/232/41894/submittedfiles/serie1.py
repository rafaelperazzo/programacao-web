# -*- coding: utf-8 -*-
import math
a=float(input('Digite o valor de a: '))
a=int(a)
b=float(input('Digite o valor de b: '))
b=int(b)
contador=0
x=a
while x<=b:
    derivada=(math.cos(x))-(math.exp(x))
    if derivada<0:
        contador=contador+1
    x=x+0.01
if contador==0:
    print('SIM')
else:
    print('NAO')

