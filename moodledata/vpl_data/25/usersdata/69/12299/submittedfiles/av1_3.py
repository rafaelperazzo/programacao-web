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
    cont=cont+1
    if dividendo%divisor=!0:
        resto=dividendo%divisor
    else:
        print(resto)
print (cont)
