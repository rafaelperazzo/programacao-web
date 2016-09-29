# -*- coding: utf-8 -*-
from __future__ import division
import math
cv=input('numero de vitorias do Cormengo:')
ce=input('numero de empates do Cormengo:')
cs=input('saldo de gols do Cormengo:')
fv=input('numero de vitorias do flainthians:')
fe=input('numero de empates do flainthians:')
fs=input('saldo de gols do flainthians:')
if 3*cv+ce>3*fv+fe:
    input('C')
elif 3*cv+ce<3*fv+fe:
    input('F')
elif 3*cv+ce==3*fv+fe:
    if cs>fs:
        print('C')
    elif cs<fs:
        print ('F')
    else:
        print('=')

