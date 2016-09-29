# -*- coding: utf-8 -*-
from __future__ import division
import math

C1= input('numero de vitorias do Cormengo: ')
C2= input('numero de empates do Cormengo: ')
C3= input('saldo de gols do Cormengo: ')
F1= input('numero de vitorias do Flaminthians: ')
F2= input('numero de epates do Flaminthians: ')
F3= input('saldo de gols do Flaminthians: ')

C=(C1*3)+(C2)
F=(F1*3)+(F2)

if C>F or C==F and C3>F3:
    print('C')
else:
    print('F')
