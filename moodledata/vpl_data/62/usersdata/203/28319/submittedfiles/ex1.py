# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
Delta=(b*b)-(4*a*c)
if Delta>=0:
    x1=(-1*b+(Delta)**1/2)/2*a
    x2=(-1*b-(Delta)**1/2)/2*a
    print('%f' %x1)
    print('%f' %x2)
else Delta>=0:
    print("Não existem raiz reais")