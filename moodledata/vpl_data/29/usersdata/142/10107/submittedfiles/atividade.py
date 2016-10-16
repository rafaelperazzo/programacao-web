# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite um numero n:'))
contador=1
while n//10!=0:
    n=n//10
    contador = contador+1
print contador