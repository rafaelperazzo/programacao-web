# -*- coding: utf-8 -*-
import math
cv=int(input('digite cv:'))
ce=int(input('digite ce:'))
cs=int(input('digite o cs:'))
fv=int(input('digite o fv:'))
fe=int(input('digite o fe:'))
fs=int(input('digite o fs:'))
if cv>fv:
    print('F')
else:
    print('C')
if ce>fe:
    if cs>fs:
        print('C')
else:
    print('F')
if cv>fv and ce>fe and cs==fe:
    print('=')
