# -*- coding: utf-8 -*-
from __future__ import division
import math
n = int(input('n:'))
a = int(input('a:'))
b = int(input('b:'))
cont=0
x = 1
while cont<=n:
    if x%a==0 or x%b==0:
        print(x)
        cont = cont+1
        x=x+1
    else:
        x=x+1
    
    
