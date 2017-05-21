# -*- coding: utf-8 -*-
import math
a=int(input('digite o primeiro inteiro positivo:'))
b=int(input('digite o segundo inteiro positivo:'))
if a>b:
    menor=b
else:
    menor=a
for i in range(1,menor+1,1):
    if a%i==0 and b%i==0:
        MDC=i