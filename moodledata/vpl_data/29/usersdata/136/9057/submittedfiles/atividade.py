# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite o valor de n:')

i = 1

cont = 0

while i<n:

    if i%2==1:

        cont = cont + 1

    i = i + 1

print (cont)