# -*- coding: utf-8 -*-
from __future__ import division
import math
n = int(input('Digite n:'))
x1 = int(input('Digite a coordenada em x para a figura 1:'))
y1 = int(input('Digite a coordenada em y para a figura 1:'))
x2 = int(input('Digite a coordenada em x para a figura 2:'))
y2 = int(input('Digite a coordenada em y para a figura 2:'))

if n%2==0:
    if (x1<=(n/2) and x2>(n/2)) or (x2<=(n/2) and x1>(n/2)):
        print ('S')
    elif (y1<=(n/2) and y2>(n/2)) or (y2<=(n/2) and y1>(n/2)):
        print ('S')
    else:
        print('N')
else:
    print ('N')
            
            
