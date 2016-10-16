# -*- coding: utf-8 -*-
from __future__ import division
import math

N=input('Digite o valor de N:')
for i in range (0,N,1):
    X=input('Digite o valor de X:')
    Y=input('Digite o valor de Y:')
    if X>=0 and Y>=0 and (((X**2)+(Y**2))<=1):
        print ('SIM')
    else:
        print ('NÃO')
        