# -*- coding: utf-8 -*-
import math
def inteiroPositivo():
    x = int(input('Informe o valor: '))
    while x<0:
        x = int(input('Informe o valor: '))
    return x

a = inteiroPositivo();
b = inteiroPositivo();

#A fim de poupar tempo, só vai até o mínimo entre a e b
for i in range (1, min(a, b)):
    if a%i == 0 and b%i == 0:
        mdc = i

print(mdc)

