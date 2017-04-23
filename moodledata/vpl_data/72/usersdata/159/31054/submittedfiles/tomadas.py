# -*- coding: utf-8 -*-
import math

T1=int(input('Número de tomadas da 1ª régua:'))
T2=int(input('Número de tomadas da 2ª régua:'))
T3=int(input('Número de tomadas da 3ª régua:'))
T4=int(input('Número de tomadas da 4ª régua:'))
a=(T1-1)+(T2-1)+(T3-1)+T4
print('Número máximo de notebooks: %d' %a)