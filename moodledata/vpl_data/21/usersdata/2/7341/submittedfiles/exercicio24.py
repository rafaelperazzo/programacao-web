# -*- coding: utf-8 -*-
from __future__ import division
import math

a = input('Digite o número 1: ')
b = input('Digite o número 2: ')

mdc  = 1

for i in range(1,a+1,1):
    if a%i==0 and b%i==0:
        mdc = i

print mdc