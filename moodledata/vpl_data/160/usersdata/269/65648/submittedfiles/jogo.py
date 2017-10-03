# -*- coding: utf-8 -*-
import math

cv=float(input('digite cv: '))
ce=float(input('digite ce: '))
cs=float(input('digite cs: '))
fv=float(input('digite fv: '))
fe=float(input('digite fe: '))
fs=float(input('digite fs: '))

c=(3*cv)+(1*ce)
f=(3*fv)+(1*fe)

if c>f:
    print('C')
if c<f:
    print('F')
if c==f:
    if cs>fs:
        print('C')
    if cs<fs:
        print('F')
    if cs==fs:
        print('=')