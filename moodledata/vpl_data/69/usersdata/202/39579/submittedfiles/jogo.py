# -*- coding: utf-8 -*-
import math
cv=int(input('digite o valor de cv:'))
ce=int(input('digite o valor de ce:'))
cs=int(input('digite o valor de cs:'))
fv=int(input('digite o valor de fv:'))
fe=int(input('digite o valor de fe:'))
fs=int(input('digite o valor de fs:'))
if ce>fe:
    if cs>fs:
        print ('C')
else:
    print ('F')
if cv>fv:
    print('F')
else:
    print ('C')
if cv>fv and ce>fe and cs==fe:
    print ('=')