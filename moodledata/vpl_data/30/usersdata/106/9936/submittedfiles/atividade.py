# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input ('Digite um número: '))
if n<0:
    n = n*(-1)
Soma = 0
a = n
i = 1
while i <= n:
    Soma = Soma + (i/a)
    i = i + 1
    a = a - 1
print ('%.5f' %Soma)