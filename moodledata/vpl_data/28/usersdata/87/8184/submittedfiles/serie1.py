# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input("valor de n:")
soma=0
i=1
j=1
while i<=n:
    if i%2==0:
        soma=soma-i/j
    else:
        soma=soma+i/j
    j=i**2
    i=i+1