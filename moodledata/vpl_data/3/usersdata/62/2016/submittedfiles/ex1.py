# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
#PROCESSAMENTO
delta=(b**2)-(4*a*c)
x=float(delta**0.5)
#SAIDA
if delta>=0:
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)
    print(x1)
    print(x2)
else:
    
    print("SRR")