# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv=input('Digite o valor de Cv:')
Ce=input('Digite o valor de Ce:')
Cs=input('Digite o valor de Cs:')
Fv=input('Digite o valor de Fv:')
Fe=input('Digite o valor de Fe:')
Fs=input('digite o valor de Fs:')

Pc=(Cv*3)+(Ce*1)
Pf=(Fv*3)+(Fe*1)
if Pc>Pf:
    print('C')
elif Pf>Pc:
    print('F')
else:
     if Cs>Fs:
         print('C')
     elif Fs>Cs :
         print('F')
     else
         print('=')
    