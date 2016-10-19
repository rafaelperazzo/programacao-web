# -*- coding: utf-8 -*-
from __future__ import division
import math

a =input('Digite a: ')
b = input('Digite b: ')

contA = 0

while a>=1:
    a = a//10
    contA = contA + 1

print contA