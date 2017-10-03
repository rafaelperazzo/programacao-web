# -*- coding: utf-8 -*-
from __future__ import division
a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))
#COMECE A PARTIR DAQUI!
delta = b*b-4*a*c
if delta < 0:
    print("SRR")
elif delta >= 0:
    x1 =(-1*b + math.sqrt(delta))/(2*a)
    x2 =(-1*b + math.sqrt(delta))/(2*a)
    print("as raizes da equacao sao",x1,"e",x2)
