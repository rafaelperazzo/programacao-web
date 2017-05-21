# -*- coding: utf-8 -*-
import math
n1=int(input('digite o primeiro numero:'))
n2=int(input('digite o segundo numero:'))
if a>b:
    menor=b
else:
    menor=a
for i in range(1,menor+1,1):
    if a%i==0 and b%i==0:
        mdc=i
print(mdc)
