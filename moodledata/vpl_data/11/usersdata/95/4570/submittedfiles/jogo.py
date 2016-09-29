# -*- coding: utf-8 -*-
from __future__ import division
import math
cv=input('Número de vitórias do Cormengo:')
ce=input('Empates:')
cs=input('Saldo de gols:')
fv=input('Número de vitórias do Flaminthians')
fe=input('Empates:')
fs=input('Saldo de gols:')

if (cv*3+ce+cs)>(fv*3+fe+cs):
    print('C')
elif (cv*3+ce+cs)<(fv*3+fe+cs):
    print('F')
else:
    print('=')
    