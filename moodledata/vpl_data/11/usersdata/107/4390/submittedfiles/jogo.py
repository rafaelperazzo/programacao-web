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
pf=(fv*3)+(fe*1)
if pc>pf:
    print('C')
if pf>pc:
    print('F')
if pf==pc:
    if cs>fs:
        print('C')
    if fs>cs:
        print('F')
    if fs==cs:
        print('=')
        