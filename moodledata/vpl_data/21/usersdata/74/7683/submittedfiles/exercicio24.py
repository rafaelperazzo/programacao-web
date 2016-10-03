# -*- coding: utf-8 -*-
from __future__ import division
import math

a = int(input('Primeiro numero: '))
b = int(input('Segundo numero: '))

for i in range(1,b+1,1):
    if a%i==0 and b%i==0:
        mdc = a/i
print('%d'% (mdc))