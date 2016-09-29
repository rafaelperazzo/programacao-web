# -*- coding: utf-8 -*-
from __future__ import division
import math
#COMECE SEU CÓDIGO AQUI

L = input(' digite a distância em que L se encontra: ')
R = input(' digite a distância em que R se encontra: ')
D = input(' digite a distância em que D se encontra: ')

if R > 50 and L < R and R > D:
    print ('S')
else:
    print ('N')