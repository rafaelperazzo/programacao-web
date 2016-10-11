# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('digite n:'))
cont=0

while n>=0:
    s=(cont/n)+(cont/(n-cont))
if n<0:
    n*(-1)
    s=(cont/n)+(cont/(n-cont))

    print(s)
cont=cont+1