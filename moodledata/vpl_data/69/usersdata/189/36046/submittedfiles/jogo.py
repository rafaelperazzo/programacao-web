# -*- coding: utf-8 -*-
import math
cv=int(input('digite o valor do Cv:'))
ce=int(input('digite o valor do Ce:'))
cs=int(input('digite o valor do Cs:'))
fv=int(input('digite o valor do Fv:'))
fe=int(input('digite o valor do Fe:'))
fs=int(input('digite o valor do Fs:'))
vc=cv*3
vf=fv*3
if (vc+ce)>(vf+fe):
    print('C')
if (vc+ce)<(vf+ce):
    print('F')
if (vc+ce)==(vf+fe):
    print('=')
