# -*- coding: utf-8 -*-
from __future__ import division
import math

def maiorDegrau(x):
    maior = 0
    for i in range (0, len(x)-1, 1):
        degrau = math.fabs(x[i]-x[i+1])
        if degrau>maior:
            maior = degrau
    return maior

n = int(input("Digite n:"))
if n>=2:
    a = []
    for i in range(0, n, 1):
        a.append(int(input("Digite os elementos de a:")))
else:
    n = int(input("Digite n:"))
print maiorDegrau(a)