# -*- coding: utf-8 -*-
import math
n = int(input('Digite o numero de multiplos desejados: '))
a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))

for x in range(a, b):
    if x % n == 0:
        print(x)
