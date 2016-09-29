# -*- coding: utf-8 -*-
from __future__ import division
import math
cv=input('digite o valor de cv:')
ce=input('digite o valor de ce:')
cs=input('digite o valor de cs:')
fv=input('digite o valor de fv:')
fe=input('digite o valor de fe:')
fs=input('digite o valor de fs:')
pc=(cv*3)+(ce*1)
pf=(cf*3)+(cf*1)
if pc>pf:
    print('c')
if pf>pc:
    print('f')
if pf==pc:
    if cs>fs:
        print('c')
    if fs>cs:
        print('f')
    
        