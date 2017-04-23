# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))
cont=0
for i in range (a,b+1,1):
    if (a%i==0):
        MDC=MDC+1
    if (b%i==0):
        MDC=MDC+1
if (MDC>=1):
    print(MDC)