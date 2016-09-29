# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=int(imput('digite o valor de n (n>0)':))
m=int(imput('digite o valor de m (m>0)':))
#PROCESSAMENTO
mdc=n
while divisor <=n:
    if n% divisor==0 and m%divisor==0:
        mdc=divisor 
    divisor+=1        
print('MDC(%d,%d)=%d'%(n,m,mdc))

