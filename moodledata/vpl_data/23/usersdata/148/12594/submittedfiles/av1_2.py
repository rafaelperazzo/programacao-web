# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite a quantidade n de linhas e colunas:')
x1=input('Qual a coordenada x1:')
y1=input('Qual a coordenada y1:')
x2=input('Qual a coordenada x2:')
y2=input('Qual a coordenada y2:')
#PROCESSAMENTO
b=n/2
a=n/2
if x1<=a and x2>a:
    print ('S')
elif x2<=a and x1>a:
    print ('S')
elif y1<=b and y2>b:
    print ('S')
elif y2<=b and y1>b:
    print ('S')
else:
    print('N')
