# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))

i = 1

while i>=a or i>=b:
    if a%i==0 and b%i==0:
        mdc = a/i
    i=i+1
print('%d'% (mdc))