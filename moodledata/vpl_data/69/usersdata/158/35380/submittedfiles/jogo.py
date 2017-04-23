# -*- coding: utf-8 -*-
import math
Cv=int(input('digite Cv:'))
Ce=int(input('digite Ce:'))
Cs=int(input('digite Cs:'))
Fv=int(input('digite Fv:'))
Fe=int(input('digite Fe:'))
Fs=int(input('digite Fs:'))
if Cv>Fv:
    print('C')
elif Cv<Fv:
    print('F')
else:
    if Ce>Fe:
        print('C')
    elif Ce<Fe:
        print('F')
    else:
        if Cs>Fs:
            print('C')
        elif Cs<Fs:
            print('F')
        else:
            print('=')