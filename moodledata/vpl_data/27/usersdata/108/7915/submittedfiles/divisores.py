# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int (input ('Digite a quantidade de múltiplos:'))
a = int (input ('Digite a:'))
b = int (input ('Digite b:'))
i=1
contador=0

while (contador<n):
    if ((i%a==0) or (i%b==0)):
        print (i)
        contador=contador+1
    i=i+1
    