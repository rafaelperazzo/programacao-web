# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite um número:'))
cont=0

while n>0:
    n=n//10
    cont=cont+1
print(cont)