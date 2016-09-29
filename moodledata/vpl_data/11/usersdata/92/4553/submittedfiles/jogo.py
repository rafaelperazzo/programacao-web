# -*- coding: utf-8 -*-
from __future__ import division
import math

cv= input('Digite o numero de vitorias do C: ')
ce= input('Digite o numero de empates do C: ')
cs= input('Digite o numero do saldo de gols do C: ')
fv= input('Digite o numero de vitorias do F: ')
fe= input('Digite o numero de empates do F: ')
fs= input('igite o numero do saldo de gols do F: ')

cv= cv*3
fv= fv*3

if (cv+ce)<(fv+fe):
    print('F')
elif (cv+ce)>(fv+fe):
    print('C')
elif (cv+ce)==(fv+fe):
    if cs<fs:
        print('F')
    elif cs>fs:
        print('C')
    else:
        print('=')