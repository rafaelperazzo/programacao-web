# -*- coding: utf-8 -*-
import math
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
N = [a1, a2, a3, a4]
cont = 0
if N[0]>N[1]:
    cont += 1
if N[len(N)-1]>N[len(N)-2]:
    cont += 1
for i in range(1,len(N)-1):
    if N[i-1]<N[i] and N[i]>N[i+1]:
        cont += 1
if cont == 1:
    print("S")
else:
    print("N")