# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n:')
i=1
while i<=n:
    S=i/(i**2)
    i=i+1
print('%.5f'%S)