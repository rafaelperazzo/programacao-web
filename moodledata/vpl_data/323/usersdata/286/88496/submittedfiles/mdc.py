# -*- coding: utf-8 -*-
import math

x1 = int(input("Digite o seu primeiro número: "))
x2 = int(input("Digite o seu segundo número: "))
i = 1
j = 1
while (i <= x1 and j <= x2):
    if x1 % i == 0 and x2 % j == 0:
        print(i)
    i += 1
    j += 1