# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite n: ')
i=1
digitos=0
while n/i>=1:
    digitos=digitos+1
    i=i*10
print(digitos)
