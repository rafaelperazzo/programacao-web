# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite o valor de n:')
if n<0:
    n=n*(-1)
i=0
while True:
    if i<=n:
        soma=soma+((1+i)/(n-i))
    i=i+1
    if i==(n-1):
        break