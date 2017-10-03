# -*- coding: utf-8 -*-
from __future__ import division
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
#COMECE A PARTIR DAQUI!
delta = b*b-4*a*c
if delta < 0:
    print("SRR")
elif delta == 0:
    raiz = (-1*b+math.sqrt(delta))/(2*a)
    print("a equacao so tem uma raiz",raiz)
elif delta > 0:
    x1 =(-1*b+math.sqrt(delta))/(2*a)
    x2 =(-1*b+math.sqrt(delta))/(2*a)
    print("as raizes da equacao sao",x1,"e",x2)
