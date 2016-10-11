# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
i=1
j=n
soma=0

while i<=n:
    soma=soma+i/j
    i=i+1
    j=j-1
print('%.5 f' %soma)
    
