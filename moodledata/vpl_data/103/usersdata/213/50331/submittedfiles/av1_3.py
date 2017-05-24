# -*- coding: utf-8 -*-
import math
a=int(input('Informe o primeiro número: '))
b=int(input('Informe o segundo número: '))

contadorDivisoes=1
resto=1
while resto>=0:
    resto=a%b
    a=b
    b=resto
    contadorDivisoes=contadorDivisoes+1
    quociente=b

print(quociente)
print(contadorDivisoes)