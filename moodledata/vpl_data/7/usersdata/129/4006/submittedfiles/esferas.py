# -*- coding: utf-8 -*-
from __future__ import division
import math
A=input('Digite o valor da esfera A: ')
B=input('Digite o valor da esfera B: ')
C=input('Digite o valor da esfera C: ')
D=input('Digite o valor da esfera D: ')
if A==B+C+D and D==C+B and B==C:
    print ('S')
else:
    print ('N')