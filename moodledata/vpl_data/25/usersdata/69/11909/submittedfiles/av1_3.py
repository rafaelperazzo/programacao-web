# -*- coding: utf-8 -*-
from __future__ import division
import math
a=int(input('digite o valor de a='))
b=int(input('digite o valor de b='))
cont=0
while a%b!=0:
    a=b
    b=(a%b)
    cont=cont+1
print (cont)
