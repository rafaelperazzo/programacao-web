# -*- coding: utf-8 -*-
import math
Cv=int(input('vitorias de C:'))
Ce=int(input('empates de C:'))
Cs=int(input('saldo de gols de C:'))
Fv=int(input('vitorias de F:'))
Fe=int(input('empates de F:'))
Fs=int(input('sado de gols de F:'))
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
        elif Fs>Cs:
            print('F')
        else:
            print('=')
    