# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite n:')
i = input('Digite i:')
j = input('Digite j: ')

cont = 0
d = 1
while(cont<n):
    if d%i==0 or d%j==0:
        cont = cont + 1
        print d
    d = d + 1

