# -*- coding: utf-8 -*-
import math
n = int(input('n: 1))
a = int(input('n: 1))
b = int(input('n: 1))
mult_a = 0
mult_b = 0
cont = 0
while cont < n:
    if mult_a < mult_b:
        print(mult_a)
        mult_a += 1
    elif mult_b < mult_a:
        print(mult_b)
        mult_b += 1
    else:
        print(mult_b)
        mult_a += 1
        mult_b += 1
    cont += 1