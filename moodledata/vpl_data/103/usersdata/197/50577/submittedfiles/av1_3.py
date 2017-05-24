# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
if a>=b:
    d=a
else:
    d=b
cont=1
divisoes=1
mdc=b
while a%d!=0:
    resto=a%d
    a=b
    b=resto
    divisoes=divisoes+1
    mdc=resto
print(mdc)
print(divisoes)
