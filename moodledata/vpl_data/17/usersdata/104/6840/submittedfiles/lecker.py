# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
c=input('Digite o valor de c:')
d=input('Digite o valor de d:')
#PROCESSAMENTO
if a>b and a>c and a>d:
    if b<c and c<d:
        print('S')
    if b<c and c>b:
        print('N')
    
