# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Quantidade de pontos: '))

i = 1

while n>=i:
    x = input('Cordenada x')
    y = input('Cordenada y')
    if (x**2+y**2)<=1 and x>=0 and y>=0:
        print('%d %d pertencem a figura'% (x)(y))
    else:
        print('%d %d não pertencem a figura'% (x)(y))
    i = i+1