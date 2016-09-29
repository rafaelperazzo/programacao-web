# -*- coding: utf-8 -*-
from __future__ import division
import math

cv=input('valor de cv:')
ce=input('valor de ce:')
cs=input('valor de cs:')
fv=input('valor de fv:')
fe=input('valor de fe:')
fs=input('valor de fs:')

cv*3
fv*3
ce*1
fe*1

if cv+ce>fv+fe:
    print('c')
elif cv+ce<fv+fe:
    print('f')
elif cv+ce==fv+fe and cs==fs:
    print('=')
    
    
