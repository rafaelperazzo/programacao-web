# -*- coding: utf-8 -*-
import math

x1 = int(input("Digite o seu primeiro número: "))
i = 1

while (i <= x1):
    if x1 % i == 0:
        print(i)
        i += 1

