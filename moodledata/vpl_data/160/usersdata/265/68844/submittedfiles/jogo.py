# -*- coding: utf-8 -*-
import math
cv = int(input('cv: '))
ce = int(input('cv: '))
cs = int(input('cs: '))
fv = int(input('fv: '))
fe = int(input('fe: '))
fs = int(input('fs: '))
c=(cv*3)+ce
f=(fv*3)+fe
if c>f:
    print(c)
if c<f:
    print(f)
if c==f:
    if cs>fs:
        print(c)
    if cs<fs:
        print(f)
    if cs==fs:
        print(=)