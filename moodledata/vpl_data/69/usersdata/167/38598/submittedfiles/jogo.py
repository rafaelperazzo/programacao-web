# -*- coding: utf-8 -*-
import math
cv=int(input('digite cv:'))
ce=int(input('digite ce:'))
cs=int(input('digite cs:'))
fv=int(input('digite fv:'))
fe=int(input('digite fe:'))
fs=int(input('digite fs:'))
if cv>fv:
    print('F')
else:
    print('C')
if ce>fe:
    if cs>fs:
        print('F')
else:
    print('C')
if cs==fe:
    print('=')  