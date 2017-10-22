# -*- coding: utf-8 -*-
import math
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
N = [a1, a2, a3, a4]
cont = 0
for i in range(0,len(N)):
    if N[i]>N[i-1] and N[i+1]>N[i]:
        cont += 1
if cont == 1:
    print("S")
else:
    print("N")