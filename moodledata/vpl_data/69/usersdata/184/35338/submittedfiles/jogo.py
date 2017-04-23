# -*- coding: utf-8 -*-
import math
cv=int(input('digite o número de vitórias do cormengo:'))
ce=int(input('digite o número de empates do cormengo:))
cs=int(input('digite o saldo de gols do cormengo:'))
fv=int(input('digite o número de vitórias do flaminthians:'))
fe=int(input('digite o número de empates do flaminthians:'))
fs=int(input('digite o saldo de gols do flaminthians:'))
pontos1=(3*cv)+(1*ce)
pontos2=(3*fv)+(1*fe)
if pontos1>pontos2:
    print('C')
elif pontos2>pontos1:
    print('F')
else:
    if cs>fs:
        print('C')
    elif fs>cs:
        print('F')
    else:
        print('=')