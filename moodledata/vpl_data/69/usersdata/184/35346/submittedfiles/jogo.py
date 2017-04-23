# -*- coding: utf-8 -*-
import math
Cv=int(input('digite o número de vitórias do cormengo:'))
Ce=int(input('digite o número de empates do cormengo:'))
Cs=int(input('digite o saldo de gols do cormengo:'))
Fv=int(input('digite o número de vitórias do flaminthians:'))
Fe=int(input('digite o número de empates do flaminthians:'))
Fs=int(input('digite o saldo de gols do flaminthians:'))
pontos1=(3*Cv)+(1*Ce)
pontos2=(3*Fv)+(1*Fe)
if pontos1>pontos2:
    print('C')
elif pontos2>pontos1:
    print('F')
else:
    if Cs>Fs:
        print('C')
    elif Fs>Cs:
        print('F')
    else:
        print('=')