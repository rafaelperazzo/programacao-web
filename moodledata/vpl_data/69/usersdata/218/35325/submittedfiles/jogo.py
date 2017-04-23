# -*- coding: utf-8 -*-
import math
Cv=int(input('digite o numero de pontos do C:'))
Ce=int(input('digite o numero de empates do C:'))
Cs=int(input('digite o saldo de gols de C:'))
Fv=int(input('digite o numero de pontos do F:'))
Fe=int(input('digite o numero de empates do F:'))
Fs=int(input('digite o saldo de gols de F:'))
if Cv>Fv:
    print('C')
elif Fv>Cv:
    print('F')
else:
    if Ce>Fe:
        print('C')
    elif Fe>Ce:
        print('F')
    else:
        if Cs>Fs:
            print('C')
        elif Fe>Ce:
            print('F')
        else:
            print('=')
