# -*- coding: utf-8 -*-
import math
x=int(input('Digite o primeiro numero:'))
y=int(input('Digite o segundo numero:'))
divisoes=1
MDC=b
while x%y!=0:
    resto=x%y
    x=y
    y=resto
    divisoes=divisoes+1
    MDC=resto
print(MDC)
print(divisoes)