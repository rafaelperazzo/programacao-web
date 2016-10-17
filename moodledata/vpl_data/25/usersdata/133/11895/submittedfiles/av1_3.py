# -*- coding: utf-8 -*-
from __future__ import division
import math
print('Calcula o MDC de dois números pelo algoritmo de Euclides')
a=input('Digite um número')
b=input('Digite um número')
r=a%b
while(r!=0):
    a=b
    b=r
    r=a%b
print(r)
