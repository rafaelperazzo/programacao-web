# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
cont=0
#PROCESSAMENTO
if a<b:
    while b%a>0:
        cont=cont+1
        x=b%a
        b=a
        a=x
print(a)
