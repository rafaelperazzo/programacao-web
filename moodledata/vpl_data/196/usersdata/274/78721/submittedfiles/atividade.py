# -*- coding: utf-8 -*-
import math
n = int(input("Digite o valor de n: "))
i = 1
numerador= 0
a = 1
s = n

if (n<0):
    n = n*-1
else:
    n = n
while (i<=n):
    s = numerador/(n+a)+s
    i = i+1
    a = a-1
print ("%.5f" % s)