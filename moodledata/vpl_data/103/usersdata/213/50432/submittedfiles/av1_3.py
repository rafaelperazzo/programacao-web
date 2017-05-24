# -*- coding: utf-8 -*-
import math
a=int(input('Informe o primeiro número: '))
b=int(input('Informe o segundo número: '))

contadorDivisoes=0

while c>0:
    c=a%b
    a=b
    b=c
    contadorDivisoes=contadorDivisoes+1
    MDC=b

print(MDC)
print(contadorDivisoes)