# -*- coding: utf-8 -*-
from __future__ import division
import math
n = int(input('Digite o valor de n:'))
a = int(input('Digite o valor de a:'))
b = int(input('Digite o valor de b:'))

i=2
contador=1
while (contador<=n):
    if (i%a==0) or (i%b==0):
        contador=contador + 1
        print (i)
    i=i+1

