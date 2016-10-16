# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int ( input ('Digite um número inteiro :'))
if n < 0:
    n = n*(-1)
if n == 0:
    n = n+1
contador = 0
while n>=1:
    contador = contador + 1
    n = n /10
print (contador)