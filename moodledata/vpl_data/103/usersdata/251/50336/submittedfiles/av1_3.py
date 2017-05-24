# -*- coding: utf-8 -*-
import math
n1=int(input('Digite o primeiro número: '))
n2=int(input('Digite o segundo número: '))
dividendo=0
divisor=0
mdc=1
divisoes=0
if n1>n2 or n1==n2:
    dividendo=n1
    divisor=n2
else:
    dividendo=n2
    divisor=n1
    
while dividendo%divisor>0:
    mdc=dividendo%divisor
    dividendo=divisor
    divisor=mdc
    divisoes=divisoes+1
print(mdc)
print(divisoes)
    