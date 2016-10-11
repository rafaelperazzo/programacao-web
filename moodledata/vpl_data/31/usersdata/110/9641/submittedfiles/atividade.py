# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite n:')
i=1
while i<=n:
    x=input('Digite x: ')
    y=input('Digite y: ')
    if x>=0 and y>=0 and x*x + y*y<=1:
        print('Pertence à figura')
    else:
        print('Não pertence à figura')
    i=i+1
