# -*- coding: utf-8 -*-
from __future__ import division
import math
cv=input('digite cv:')
ce=input('digite ce:')
cs=input('digite cs:')
fv=input('digite fv:')
fe=input('digite fe:')
fs=input('digite fs:')
if (cv+ce)>(fv+fe):
    print('C')
elif (cv+ce)<(fv+fe):
    print('F')
else:
    print('=')
