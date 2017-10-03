# -*- coding: utf-8 -*-
import math
n = int(input("Digite o valor de n: ))
if (n<0):
    n = n*-1
Soma = 0
num = 1
den = n
while (num<=n):
    Soma = Soma+(num/den)
    num = num+1
    den = den-1
print ("%.5f" % Soma)