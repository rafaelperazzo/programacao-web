# -*- coding: utf-8 -*-
import math
a=int(input('Informe o primeiro número: '))
b=int(input('Informe o segundo número: '))

contadorDivisoes=1
c=a%b
while c>=0:
    c=a%b
    a=b
    b=c
    contadorDivisoes=contadorDivisoes+1
    quociente=b

print(quociente)
print(contadorDivisoes)