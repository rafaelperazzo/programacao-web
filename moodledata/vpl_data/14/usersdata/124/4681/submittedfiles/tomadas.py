# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
T1 = int(input('Digite o número de tomadas da régua 1: '))
T2 = int(input('Digite o número de tomadas da régua 2: '))
T3 = int(input('Digite o número de tomadas da régua 3: '))
T4 = int(input('Digite o número de tomadas da régua 4: '))
a = (T1-3)+T2+T3+T4
b = (T2-3)+T1+T3+T4
c = (T3-3)+T2+T1+T4
d = (T4-3)+T2+T3+T1

if T1 >= T2 and T1 >= T3 and T1 >= T4:
    print('%d' %a)
elif T2 >= T1 and T2 >= T3 and T2 >= T4:
    print('%d' %b)
elif T3 >= T2 and T3 >= T1 and T3 >= T4:
    print('%d' %c)
elif T4 >= T2 and T4 >= T3 and T4 >= T1:
    print('%d' %d)