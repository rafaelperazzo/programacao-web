# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=input('digite o valor de Cv:')
Ce=input('digite o valor de Ce:')
Cs=input('digite o valor de Cs:')
Fv=input('digite o valor de Fv:')
Fe=input('digite o valor de Fe:')
Fs=input('digite o valor de Fs:')

if ((Cv*3)+(Ce*1)+(Cs))>((Fv*3)+(Fe*1)+(Fs)):
    print('C')
    
elif ((Cv*3)+(Ce*1)+(Cs))<((Fv*3)+(Fe*1)+(Fs)):
    print('F')
    
else:
    print('=')

