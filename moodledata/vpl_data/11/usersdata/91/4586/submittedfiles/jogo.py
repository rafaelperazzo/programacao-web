# -*- coding: utf-8 -*-
from __future__ import division
import math

cv=input('digite o valor de cv:')
ce=input('digite o valor de ce:')
cs=input('digite o valor de cs:')
fv=input('digite o valor de fv:')
fe=input('digite o valor de fe:')
fs=input('digite o valor de fs:')

if ((cv*3)+(ce*1)+(cs))>((fv*3)+(fe*1)+(fs)):
    print('c')
    
elif ((cv*3)+(ce*1)+(cs))==((fv*3)+(fe*1)+(fs)):
    print('=')
    
elif ((cv*3)+(ce*1)+(cs))<((fv*3)+(fe*1)+(fs)):
    print('f')
    

