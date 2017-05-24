# -*- coding: utf-8 -*-
import math
x=int(input('digite um numero:'))
y=int(input('digite um numero:'))
contador=contador+1
while x%y!=0:
    resto=x%y
    x=y
    y=resto
    contador=contador+1
    mdc=resto
print