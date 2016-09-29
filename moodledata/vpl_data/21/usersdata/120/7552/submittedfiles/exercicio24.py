# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=int(input('digite o valor de n':))
m=int(input('digite o valor de m ':))
#PROCESSAMENTO
mdc=n
while divisor <=n:
    if n% divisor==0 and m%divisor==0:
        mdc=divisor 
    divisor+=1        
print('MDC(%d,%d)=%d'%(n,m,mdc))

