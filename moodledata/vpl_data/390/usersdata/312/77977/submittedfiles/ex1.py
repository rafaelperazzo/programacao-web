# -*- coding: utf-8 -*-
from math import sqrt
a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))
Delta=b*b-4*a*c
if Delta < 0:
    print("SRR")
elif Delta >= 0:
    x1 =(-1*b+math.sqrt(Delta))/(2*a)
    x2 =(-1*b+math.sqrt(Delta))/(2*a)
    print("as raizes da equacao sao",x1,"e",x2)
