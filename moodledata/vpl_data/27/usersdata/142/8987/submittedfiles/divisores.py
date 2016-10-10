# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int(input('Digite n:'))
a = int(input('Digite a:'))
b = int(input('Digite b:'))

cont = 1
x = 1
while cont<=n:
    if x%a==0 or x%b==0:
        print x
        cont = cont+1
    else:
        x=x+1