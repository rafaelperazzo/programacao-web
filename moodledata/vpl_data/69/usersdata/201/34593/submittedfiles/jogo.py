# -*- coding: utf-8 -*-
import math
Cv=int(input('Numero de vitorias do Cormengo:'))
Ce=int(input('Numero de empates do Cormengo:'))
Cs=int(input('Saldo de gols do Cormengo:'))
Fv=int(input('Numero de vitorias do Flaminthians:'))
Fe=int(input('Numero de empates do Flaminthians:'))
Fs=int(input('Saldo de gols do Flaminthians:'))
PC=Cv*3+Ce
PF=Fv*3+Fe
if PC>PF:
    print('C')
elif PF>PC:
    print('F')
elif Cs>Fs:
    print('C')
elif 