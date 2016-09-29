# -*- coding: utf-8 -*-
from __future__ import division
import math
cv=input('Vitórias de C: ')
ce=input('Empates de C: ')
cs=input('Saldos de gol de C: ')
fv=input('Vitórias de F: ')
fe=input('Empates de F: ')
fs=input('Saldos de gol de F: ')
if (cv*3)+ce>(fv*3+fe):
    print('C')
elif (cv*3)+ce<(fv*3+fe):
    print('F')
if (cv*3)+ce==(fv*3+fe) and cs>fs:
    print('C')
elif  (cv*3)+ce==(fv*3+fe) and cs<fs: 
    print('F')
else: 
    print('=')

