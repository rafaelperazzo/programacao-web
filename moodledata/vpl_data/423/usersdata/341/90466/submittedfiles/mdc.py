# -*- coding: utf-8 -*-
import math

x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))
n=1

while (n<=x):
    if(x%n)==0 and (y%n)==0:
        MDC=n
    n = n + 1
print(MDC)

