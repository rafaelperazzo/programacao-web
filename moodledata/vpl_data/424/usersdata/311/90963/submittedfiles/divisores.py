# -*- coding: utf-8 -*-
import math
n = int(input())
a = int(input())
b = int(input())

for x in range(a, b):
    if x % n == 0:
        print(x)
