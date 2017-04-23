# -*- coding: utf-8 -*-
import math
cv=int(input('digite cv:'))
ce=int(input('digite ce:'))
cs=int(input('digite cs:'))
fv=int(input('digite fv:'))
fe=int(input('digite fe:'))
fs=int(input('digite fs:'))
if cv>fv:
    print('C')
elif cv<fv:
    print('F')
elif ce>fe:
    print('C')
elif ce<fe:
    print('F')
elif cs>fs:
    print('C')
elif cs<fs:
    print('F')
