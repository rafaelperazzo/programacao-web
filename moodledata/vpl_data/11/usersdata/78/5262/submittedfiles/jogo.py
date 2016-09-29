# -*- coding: utf-8 -*-
from __future__ import division
import math

cv=input('digite o número de vitórias:')
ce=input('digite o número de empates:')
cg=input('digite o número de gols:')
fv=input('digite o número de vitórias:')
fe=input('digite o número de empates:')
fg=input('digite o número de gols:')

cv=cv*3
fv=fv*3
tc=cv+ce+cg
tf=fv+fe+fg

if tc<tf:
    print('F')
    else tf<tc:
        print('c')
if tc==tf:
    print('=')