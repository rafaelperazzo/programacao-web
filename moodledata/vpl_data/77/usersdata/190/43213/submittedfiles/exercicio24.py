# -*- coding: utf-8 -*-
import math
a=int(input('digite o número: '))
b=int(input('digite o número: '))
if a>b:
    menor=b
else:
    menor=b
for i in range (1,(menor+1),1):
    if a%i==0 and b%i==0:
        MDC=i
print (MDC)
