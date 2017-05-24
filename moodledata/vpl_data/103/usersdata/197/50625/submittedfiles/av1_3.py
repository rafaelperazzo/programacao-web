# -*- coding: utf-8 -*-
import math
a=int(input('Digite o primeiro numero:'))
b=int(input('Digite o segundo numero:'))
divisoes=1
MDC=b
while a%b!=0:
    resto=a%b
    a=b
    b=resto
    divisoes=divisoes+1
    MDC=resto
print(MDC)
print(divisoes)