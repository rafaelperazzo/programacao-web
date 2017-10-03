# -*- coding: utf-8 -*-
import math
#ENTRADA
n = int(input('Digite o valor de n: '))
if (n<0) :
    n = n*-1
SOMA = 0
num = 1
den = n

while (num<=n) :
    SOMA = SOMA+(num/den)
    num = num+1
    den = den - 1
print('%.5f' % SOMA)

