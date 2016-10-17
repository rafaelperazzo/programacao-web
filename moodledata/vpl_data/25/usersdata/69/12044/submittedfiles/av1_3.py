# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('digite o valor de a='))
b=int(input('digite o valor de b='))
cont=1
resto=a%b
while resto!=0:
    a=b
    b=resto
    resto=a%b
    cont=cont+1
print(resto)
print (cont)
