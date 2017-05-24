# -*- coding: utf-8 -*-
import math
a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
if a>=b:
    x1=a
    x2=b
else:
    x1=b
    x2=a
MDC=0
cont=0
divisoes=b
while MDC==0:
    cont=cont+1
    if a%x2==0 and b%x2==0:
        MDC=x2
    else:
        x2=x2-1
divisoes=divisoes-cont
print(MDC)
print(divisoes)