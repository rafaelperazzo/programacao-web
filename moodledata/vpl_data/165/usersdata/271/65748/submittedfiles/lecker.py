# -*- coding: utf-8 -*-
import math
#ENTRADA
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
d = float(input('Digite o valor de d: '))
#PROCESSAMENTO
if (a<b) and (b<c) and (c<d) :
    print('S')
elif (a<b) and (c<b) and (d<c):
    print('S')
