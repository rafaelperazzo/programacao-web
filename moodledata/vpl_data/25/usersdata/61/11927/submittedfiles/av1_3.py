# -*- coding: utf-8 -*-
from __future__ import division
import math
x=input('Digite um número real: ')
y=input('Digite um número real: ')
anterior=x
atual=y
resto=(anterior%atual)
while resto!=0:
    anterior=atual
    atual=resto
    resto=(anterior%atual)
print ('MDC(%d,%d).%d'%(x,y,atual))