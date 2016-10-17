# -*- coding: utf-8 -*-
from __future__ import division
import math
dividendo=int(input('digite o valor do dividendo='))
divisor=int(input('digite o valor do divisor='))
cont=1
resto=dividendo%divisor
while resto!=0:
    dividendo=divisor
    divisor=resto
    resto=dividendo%divisor
    cont=cont+1
    if resto==0:
        print(resto)
print (cont)
