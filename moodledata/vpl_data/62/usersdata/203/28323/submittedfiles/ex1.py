# -*- coding: utf-8 -*-
from __future__ import division
a = float(input('Digite a: '))
b = float(input('Digite b: '))
c = float(input('Digite c: '))
#COMECE A PARTIR DAQUI!
Delta=(b**2)-(4*(a)*(c))
if Delta>=0:
    x1=(-1*b+(Delta)**1/2)/2*a
    x2=(-1*b-(Delta)**1/2)/2*a
    print('x1=%f' %x1)
    print('x2=%f' %x2)
else:
    print("Não existem raiz reais")