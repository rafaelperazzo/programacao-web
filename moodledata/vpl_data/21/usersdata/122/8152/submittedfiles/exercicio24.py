# -*- coding: utf-8 -*-
from __future__ import division
import math

#ENTRADA

a=input('Digite o valor de a:')
b=input('Digite o valor de b:')

#PROCESSAMENTO

for i in range (1,(a*b),1):
    if i%a==0 and i%b==0 and i/a>1 and i/b>1:
        print(i)