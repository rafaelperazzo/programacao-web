# -*- coding: utf-8 -*-
import math
cv=float(input('digite Cv:'))
ce=float(input('digite Ce:'))
cs=float(input('digite Cs:'))
fv=float(input('digite Fv:'))
fe=float(input('digite Fe:'))
fs=float(input('digite Fs:'))
pc=(fv*3)+ce*1
pf=(fv*3)+fe*1
if pc>pf:
    print('C')
elif pf>pc:
    print('F')
elif pf==pc and cs>fs:
    print('C')
elif pf==pc and cs<fs:
    print('F')
else:
    print('=')