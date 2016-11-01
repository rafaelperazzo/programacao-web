# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
#PROCESSAMENTO
if a>b:
    if (c%a)%b!=0:
        print ('N')
    else:
    a=c//a
    b=(c%a)//b
else:
    if (c%b)%a!=0:
        print('N')
    b=c//b
    a=(c%b)//a
print(a)
print(b)


        