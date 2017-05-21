# -*- coding: utf-8 -*-
import math
a=int(input('Informe o 1° número: '))
b=int(input('Informe o 2° número: '))

if a>b:
    menor=b
else:
    menor=a

MDC=0

for i in range(1,(menor+1),1):
    if a%i==0 and b%i==0:
        MDC=i
print(MDC)
