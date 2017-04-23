# -*- coding: utf-8 -*-
import math
Cv=int(input('vitorias de C:'))
Ce=int(input('empates de C:'))
Cs=int(input('saldo de gols de C:'))
Fv=int(input('vitorias de F:'))
Fe=int(input('empates de F:'))
Fs=int(input('sado de gols de F:'))
if (Cv*3+Ce*1)>(Fv*3+Fe*1):
    print('C')
if (Cv*3+Ce*1)<(Fv*3+Fe*1):
    print('F')
else:
        if Cs>Fs:
            print('C')
        elif Fs>Cs:
            print('F')
        else:
            print('=')
    