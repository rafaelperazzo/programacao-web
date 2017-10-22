# -*- coding: utf-8 -*-
import math

x1 = int(input("Digite o seu primeiro número: "))
x2 = int(input("Digite o seu segundo número: "))
i = 1

while (i <= x1):
    if x1 % i == 0:
        i += 1
    break
j = 1

while (j <= x2):
    if x2 % j == 0:
        j += 1
    break

