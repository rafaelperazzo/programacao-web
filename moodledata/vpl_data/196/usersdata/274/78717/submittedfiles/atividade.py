# -*- coding: utf-8 -*-
import math
n = int(input("Digite o valor de n: ))
SOMA = 0
num = 1
den = n

if (n<0):
    n = n*-1

while (num<=n):
    SOMA = SOMA+(num/den)
    num = num+1
    den = den - 1
print ("%.5f" % SOMA)