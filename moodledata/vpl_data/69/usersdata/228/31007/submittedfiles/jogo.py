# -*- coding: utf-8 -*-
import math
Cv=int(input('digite o número de vitórias do time C:'))
Ce=int(input('digite o número de empates do time C:'))
Cs=int(input('digite o saldo de gols do time C:'))
Fv=int(input('digite o número de vitórias do time F:'))
Fe=int(input('digite o número de empates do time F'))
Fs=int(input('digite o saldo de golsdo time F'))
if (Cv*3)+(Ce*1)>(Fv*3)+(Fe*1):
    print('C')
elif (Fv*3)+(Fe*1)>(Cv*3)+(Ce*1):
    print('F')
else:
    print('=')
