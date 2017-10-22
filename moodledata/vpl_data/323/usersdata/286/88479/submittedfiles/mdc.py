# -*- coding: utf-8 -*-
import math

x1 = int(input("Digite o número maior: "))
x2 = int(input("Digite o número menor: "))
i = 0
h = 0
while (i <= x1 and h <= x2):
    if x1 % i == 0 and x2 % h == 0:
        print(i)    
        i += 1
        h += 1