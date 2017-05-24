# -*- coding: utf-8 -*-
from __future__ import division
a=float(input('digite o valor de a:'))
b=float(input('digite o valor de b:'))
c=float(input('digite o valor de c:'))
cont=0
quant_a=c//a
quant_b=0
while quant_a>=0:
    troco=c-quant_a*a
    if troco%b==0:
        quant_b=troco//b
        cont=cont+1
        break
    else:
        quant_a=quant_a-1
if cont>0:
    print(quant_a)
    print(quant_b)
else:
    print('N')