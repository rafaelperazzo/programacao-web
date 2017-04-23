# -*- coding: utf-8 -*-
import math

T1=int(input('digite o número de tomadas da régua:'))
T2=int(input('digite o número de tomadas da régua:'))
T3=int(input('digite o número de tomadas da régua:'))
T4=int(input('digite o número de tomadas da régua:'))
T1=T1-2
T2=T2-2
T3=T3-2
T4=T4-1
tomadastotal=(T1+T2+T3+T4)
print('o valor de tomadastotal é:%.d'%tomadastotal)