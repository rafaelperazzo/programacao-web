# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
cont=1
x=1
while a%b!=0:
    resto=a%b
    a=b
    b=resto
    x=x+1
    mdc=resto
print(mdc)
print(x)
