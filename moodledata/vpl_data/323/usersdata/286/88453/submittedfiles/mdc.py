# -*- coding: utf-8 -*-
import math

x1 = int(input("Digite o número maior: "))
x2 = int(input("Digite o número menor: "))
i = 1

while (i <= x1):
    if x1 % i == 0:
        i += 1
    while (i <= x2):
        if x2 % i == 0:
        print(i)
    

