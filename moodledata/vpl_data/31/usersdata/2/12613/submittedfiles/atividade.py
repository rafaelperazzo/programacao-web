# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite n: ')


for i in range(1,n+1,1):
    x = input('Digite x: ')
    y = input('Digite y: ')
    if x>=0 and y>=0 and (x**2+y**2)<=1:
        print('Sim')
    else:
        print('Não')
