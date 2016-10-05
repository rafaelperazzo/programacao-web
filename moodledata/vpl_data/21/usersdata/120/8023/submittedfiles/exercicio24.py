# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=int(input('digite o valor do primeiro numero :'))
m=int(input('digite o valor do segundo numero :'))
#PROCESSAMENTO
mdc=1
divisor=2
while (divisor <=n):
    if n% divisor==0 and m%divisor==0:
        mdc=divisor 
    divisor= divisor + 1        
print('MDC(%d,%d)=%d'%(n,m,mdc))

