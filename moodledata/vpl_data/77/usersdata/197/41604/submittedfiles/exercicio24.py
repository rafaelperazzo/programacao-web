# -*- coding: utf-8 -*-
import math
x1=int(input('Digite o primeiro número:'))
x2=int(input('Digite o segundo número:'))
if x2<=x1:
    x=x2
else:
    x=x1
cont=0
while cont!=1:
    if x1%x==0 and x2%x==x1%x:
        cont=1
        mdc=x
    else:
        x=x-1
print(n)