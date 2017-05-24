# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
if b<=a:
    x=b
else:
    x=a
cont=0
while cont!=1:
    if a%x==0 and b%x==a%x:
        cont=1
        mdc=x
    else:
        x=x-1
print(x)