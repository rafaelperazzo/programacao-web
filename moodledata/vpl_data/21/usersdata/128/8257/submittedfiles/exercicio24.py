# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o primeiro número: '))
b=int(input('Digite o segundo número: '))

if a>b:
    for i in range (a, 2, (-1)):
        if a%i==0 and b%i==0:
            print (i)
            break

else:
    for i in range (b, 2, (-1)):
        if a%i==0 and b%i==0:
            print (i)
            break