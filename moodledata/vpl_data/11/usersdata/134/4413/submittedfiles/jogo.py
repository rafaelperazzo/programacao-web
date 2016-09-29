# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv = input('Número de vitórias de C:')
Ce = input('Número de empates de C:')
Cs = input('Saldo de gols de C:')
Fv = input('Número de vitórias de F:')
Fe = input('Número de empates de F:')
Fs = input('Saldo de gols de F:')

Pc = (Cv*3)+(Ce*1)
Pf = (Fv*3)+(Fe*1)
if Pc>Pf:
    print('C')
elif Pf>Pc:
    print('F')
elif Pc==Pf:
    if Cs>Fs:
        print('C')
    elif Fs>Cs:
        print('F')
elif Pc==Pf and Cs==Fs:
    print('=')
