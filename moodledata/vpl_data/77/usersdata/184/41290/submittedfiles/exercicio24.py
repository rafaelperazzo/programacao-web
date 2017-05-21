# -*- coding: utf-8 -*-
import math
n1=int(input('digite o primeiro numero:'))
n2=int(input('digite o segundo numero:'))
if n1>n2:
    menor=n2
else:
    menor=n1
for i in range(1,menor+1,1):
    if n1%i==0 and n2%i==0:
        mdc=i
print(mdc)
