# -*- coding: utf-8 -*-
import math
Cv=int(input('digite o valor do Cv:'))
Ce=int(input('digite o valor do Ce:'))
Cs=int(input('digite o valor do Cs:'))
Fv=int(input('digite o valor do Fv:'))
Fe=int(input('digite o valor do Fe:'))
Fs=int(input('digite o valor do Fs:'))
cv=Cv*3
fv=Fv*3
if cv+Ce>fc+fe:
    print('C')
if cv+Ce<fc+Fe:
    print('F')
if cv+Ce==fc+Fe:
    print('=')
