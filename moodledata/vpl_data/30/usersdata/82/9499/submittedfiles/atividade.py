# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
if n<0:
    n=n*(-1)
i=1
j=n
soma=0

while i<=n:
    soma=soma+i/j
    i=i+1
    j=j-1
    
print('%.5f' %soma)
    
