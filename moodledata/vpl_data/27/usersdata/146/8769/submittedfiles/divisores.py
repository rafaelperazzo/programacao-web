# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('digite a quantidade de divisores: ')
a = int(input('digite o valor do primeiro: '))
b = int(input('digite o valor do primeiro: '))

multi = 1
cont = 0

while cont < n:
    if multi%a == 0 or multi%b == 0:
        print (multi)
        cont = cont + 1
    multi= multi + 1