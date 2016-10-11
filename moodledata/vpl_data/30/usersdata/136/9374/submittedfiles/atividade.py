# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input("Digite o valor de n:")
i = 1
a = 0
soma = 0

if i<0:
    n=n*(-1)
while i <= n:
    soma = soma + (i/n-i)
    
print("%.5f"%soma)