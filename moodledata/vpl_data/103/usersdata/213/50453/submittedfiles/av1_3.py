# -*- coding: utf-8 -*-
import math
a=int(input('Informe o primeiro número: '))
b=int(input('Informe o segundo número: '))

contadorDivisoes=0
resto=0
MDC=0

while resto>0:
    resto=a%b
    a=b
    b=resto
    contadorDivisoes=contadorDivisoes+1
    MDC=b

print(MDC)
print(contadorDivisoes)