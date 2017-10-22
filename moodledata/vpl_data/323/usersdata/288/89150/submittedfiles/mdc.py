# -*- coding: utf-8 -*-
import math
x=int(input('Digite um numero x: '))
y=int(input('Digite um numero y: '))
while (x%y)!=0:
    resto=(x%y)
    x=y
    y=resto
    resto=(x%y)
    print ('%d' %y)