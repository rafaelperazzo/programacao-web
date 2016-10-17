# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Ddigite o número de linhas e colunas:')
x1=input('x1:')
x2=input('x2:')
y1=input('y1:')
y2=input('y2:')
n%2==0
d=((y2-y1)**2)+((x2-x1))**(1/2)
if d/2==0:
    print ('s')
else:
    print('n')
