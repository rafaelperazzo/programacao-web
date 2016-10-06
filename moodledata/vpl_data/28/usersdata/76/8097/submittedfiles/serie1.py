# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite o valor de n: ')
soma = 0
i = 1
j = 1
while i<=n:
    if i%2==0:
        soma=soma-1/j
    else:
        soma=soma+1/j
    j=j+1
    i=i+1
    print('%.5f' %soma)