# -*- coding: utf-8 -*-
import math
Cv=int(input('digite o úmero de vitórias do Cormengo:'))
Ce=int(input('digite o número de empates do Cormengo:'))
Cs=int(input('digite o saldo de gols do Cormengo:'))
Fv=int(input('digite o úmero de vitórias do Flaminthians:'))
Fe=int(input('digite o úmero de empates do Flaminthians:'))
Fs=int(input('digite o saldo de gols do Flaminthians:'))
npontosC=(3*Cv)+(1*Ce)+(1*Cs)
npontosF=(3*Fv)+(1*Fe)+(1*Fs)
if npontosC>npontosF:
    print('C')
elif npontosF>npontosC:
    print('F')
else:
    print('=')
