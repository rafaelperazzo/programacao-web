# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n:')
Cont=0

while True:
    if i%2==0:
        i=(i*(-1))
a=i//(i**2)
cont=cont+1
i=i+1
if cont==n:
    break