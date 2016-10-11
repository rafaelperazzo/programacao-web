# -*- coding: utf-8 -*-
from __future__ import division
import math

valor = int(input('Digite o valor: '))

i = 1

while valor >= i:
    valor = valor//10

    i = i+1
    
print (i)
