# -*- coding: utf-8 -*-
import math
P=int(input('Digite a posição da portinha P: '))
R=int(input('Digite a posição da portinha R: '))
if (P==1) and (R==1):
    print('A')
elif (P==1) and (R==0):
    print('B')
else:
    print('C')
