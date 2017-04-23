# -*- coding: utf-8 -*-
import math
Cv=int(input('Número de vitórias do Cormengo: '))
Ce=int(input('Número de empates do Cormengo: '))
Cs=int(input('Saldo de gols do Cormengo: '))
Fv=int(input('Número de vitórias do Flaminthians: '))
Fe=int(input('Número de empates do Flaminthians: '))
Fs=int(input('Saldo de gols do Flaminthians: '))
PontosC= Cv+Ce+Cs
PontosF= Fv+Fe+Fs
if PontosC>PontosF:
    print('C')
elif PontosF>PontosC:
    print('F')
else:
    if Cs>Fs:
        print('C')
    elif Cs<Fs:
        print('F')
    else:
        print('=')
