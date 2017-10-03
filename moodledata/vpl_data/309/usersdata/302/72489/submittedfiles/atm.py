# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
v = int(input('Valor a ser sacado: '))
if v >= 20:
    m = v//20
    n = v%20
    print(m)
if n >= 10:
    o = n//10
    p = n%10
    print(o)
if p >=5:
    r = p//5
    s = p%5
    print(r)

