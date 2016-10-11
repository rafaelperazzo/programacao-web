# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite um número: ')

i=1
cont=0
while True:
    if n//i>=1:
        cont=cont+1
        i=i*10
    else:
        break
print cont
