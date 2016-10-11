# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input("Digite o valor de n:")
i = 1
soma = 0

while i<=n:
    if i%2==0:
        soma = soma + (i/(n-i))
    i = i+1
print("%.5f"%soma)