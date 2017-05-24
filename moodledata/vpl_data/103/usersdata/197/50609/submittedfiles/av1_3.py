# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
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