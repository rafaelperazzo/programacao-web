# -*- coding: utf-8 -*-
import math
Cv=int(input('Digite o número de pontos de C:'))
Ce=int(input('Digite o número de empates de C:'))
Cs=int(input('Digite o saldo de gols de C:'))
Fv=int(input('Digite o número de pontos de F:'))
Fe=int(input('Digite o número de empates de F:'))
Fs=int(input('Digite o saldo de gols de F:'))
if Cv>Fv:
    print('F')
elif Fv>Cv:
    print('C')
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