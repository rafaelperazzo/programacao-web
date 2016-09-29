# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

Ta=input('Digite a quantidade de tomadas:')
Tb=input('Digite a quantidade de tomadas:')
Tc=input('Digite a quantidade de tomadas:')
Td=input('Digite a quantidade de tomadas:')

T1=Ta-Ta%1
T2=Tb-Tb%1
T3=Tc-Tc%1
T4=Td-Td%1

QT=(T1+T2+T3+T4)-3
print('%.d'%QT)