# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('digite o valor de n:')
soma=0
i=1
#SAIDA
if (n>=0):
    n=n*(-1)
while (n>=1):
    soma=soma+(i)/(n-(i-1))
    i=i+1
print soma    
    
