# -*- coding: utf-8 -*-
from __future__ import division
import math
Cv=input('Digite o valor de Cv:')
Ce=input('Digite o valor de Ce:')
Cs=input('Digite o valor de Cs:')
Fv=input('Digite o valor de Fv:')
Fe=input('Digite o valor de Fe:')
Fs=input('Digite o valor de Fs:')



if Cv>Fv:
    print ('C')
elif Cv<Fv:
    print ('F')
elif Cv==Fv:
    print ('=')