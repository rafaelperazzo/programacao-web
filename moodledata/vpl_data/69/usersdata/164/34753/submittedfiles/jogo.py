# -*- coding: utf-8 -*-
import math
Cv=int(input('Número de vitórias do Cormengo: '))
Ce=int(input('Número de empates do Cormengo: '))
Cs=int(input('Saldo de gols do Cormengo: '))
Fv=int(input('Número de vitórias do Flaminthians: '))
Fe=int(input('Número de empates do Flaminthians: '))
Fs=int(input('Saldo de gols do Flaminthians: '))
Cv= Cv*3
Fv= Fv*3
Ct= Cv+Ce
Ft= Fv+Fe
if (Ct>Ft):
    print('C')
elif (Ft>Ct):
    print('F')
else:
    print('=')