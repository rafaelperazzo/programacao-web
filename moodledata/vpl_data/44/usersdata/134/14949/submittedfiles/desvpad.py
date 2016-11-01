# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo
n = input('Digite o valor de n:')
a = []
soma = 0
for i in range (0,n,1):
    a.append(input('Digite o elemento:'))
    soma = soma + a[i]
media = soma/n
