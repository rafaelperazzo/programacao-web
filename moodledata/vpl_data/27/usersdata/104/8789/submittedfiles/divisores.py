# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite o valor de n:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
#PROCESSAMENTO
for i in range(1,n+1,1):
    if a%i==0 or b%i==0 or i%(a*b)!=0:
        print(i)

