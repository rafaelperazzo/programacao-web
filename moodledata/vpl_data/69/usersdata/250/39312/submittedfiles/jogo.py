# -*- coding: utf-8 -*-
import math
Cv=int(input('vitorias do cormengo:'))
Ce=int(input('empates do cormengo:'))
Cs=int(input('saldo de gols do cormengo:'))
Fv=int(input('vitorias do flaminthians:'))
Fe=int(input('empates do flaminthians:'))
Fs=int(input('saldo de gols do flaminthians:'))
pC=(Cv*3)+(Ce*1)
pF=(Fv*3)+(Fe*1)
if pC>pF:
    print('C')
elif pC<pF:
    print('F')
elif Cs>Fs:
    print('C')
elif Cs<Fs:
    print('F')
else:
    print('=')

