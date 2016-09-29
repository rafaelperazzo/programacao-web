# -*- coding: utf-8 -*-
from __future__ import division
import math

cv = input('')
ce = input('')
cs = input('')
fv = input('')
fe = input('')
fs = input('')

pc = (cv*3)+ce
pf = (fv*3)+fe

if pc>pf:
    print('C')
elif pf>pc:
    print('F')
elif cs>fs:
    print('C')
elif fs>cs:
    print('F')
else:
    print('=')