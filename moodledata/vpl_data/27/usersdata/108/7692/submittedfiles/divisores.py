# -*- coding: utf-8 -*-
from __future__ import division
import math

n = int (input ('Digite a quantidade de múltiplos:'))
a = int (input ('Digite a:'))
b = int (input ('Digite b:'))
m=0
i=1

while (m<=n):
    multA=a*i
    multB=b*i
    if (multA<multB):
        print (multA)
        print (multB)
        m=m+2
    elif (multA==multB):
        print (multA)
        m=m+1
    else:
        print (multB)
        print (multA)
        m=m+2
    
    