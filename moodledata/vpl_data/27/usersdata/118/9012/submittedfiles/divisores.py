# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('digite o número de termos:')
a = input('digite a:')
b = input('digite b:')

contador = 1
i = 1

while contador<=n:
    if i%a==0 or i%b==0:
        contador = contador +1
        print(i)
    i = i +1