# -*- coding: utf-8 -*-
import math
def inteiroPositivo():
    x = int(input('Informe o valor: '))
    while x<0:
        x = int(input('Informe o valor: '))
    return x

a = inteiroPositivo();
b = inteiroPositivo();

for i in range (min(a, b)-1):
    if a%i == 0 and b%i == 0:
        mdc = i

print(mdc)

