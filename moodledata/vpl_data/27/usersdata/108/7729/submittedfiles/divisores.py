# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int (input ('Digite a quantidade de múltiplos:'))
a = int (input ('Digite a:'))
b = int (input ('Digite b:'))
i=1
j=1

while (j<=n):
    while ((i%a==0) or (i%b==0)):
        print (i)
        i=i+1
    j=j+1
    
    