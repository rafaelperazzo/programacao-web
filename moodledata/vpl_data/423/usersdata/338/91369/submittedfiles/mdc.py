# -*- coding: utf-8 -*-
import math

u = int(input('Valor de u: '))
w = int(input('Valor de w: '))

p = 1

while (p<=u):
    if(u%p)==0 and (w%p)==0:
        MDC=p
    p = p + 1
print(MDC)
