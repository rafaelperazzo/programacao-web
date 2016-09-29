# -*- coding: utf-8 -*-
from __future__ import division
import math

#1
T1 = int(input('Digite o número de tomadas existentes na 1° regua ='))
T2 = int(input('Digite o número de tomadas existentes na 2° regua ='))
T3 = int(input('Digite o número de tomadas existentes na 3° regua ='))
T4 = int(input('Digite o número de tomadas existentes na 4° regua ='))

#2
if T1>0 and T2>0 and T3>0 and T4>0:
    T = (T1-1)+(T2-1)+(T3-1)+T4
    print(T)  


