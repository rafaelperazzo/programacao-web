# -*- coding: utf-8 -*-
import math
Cv=float(input('digite Cv : '))
Ce=float(input('digite Ce : '))
Cs=float(input('digite Cs : '))
Fv=float(input('digite Fv : '))
Fe=float(input('digite Fe : '))
Fs=float(input('digite Fs : '))
if Cv>Fv:
    print('C')
elif Fv>Cv:
    print('F')
elif Ce>Fv:
    print('C')
elif Fe>Ce:
    print('F')
elif Cs>Fs:
    print('C')
elif Fs>Cs:
    print('F')
else:
    print('=')
