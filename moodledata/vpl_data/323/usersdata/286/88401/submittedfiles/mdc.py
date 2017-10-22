# -*- coding: utf-8 -*-
import math

x1 = int(input("Digite o primeiro número: "))
x2 = int(input("Digite o segundo número: "))

i = 0

while (i <= x1):
    if x1 % i == 0:
        i += 1
    
    break
print(i)