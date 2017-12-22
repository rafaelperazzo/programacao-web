# -*- coding: utf-8 -*-
import math
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
i=1
while (i<=x):
    if (x%i) ==0 and (y%i)==0:
        MDC=i
    i=i+1
print(MDC)
