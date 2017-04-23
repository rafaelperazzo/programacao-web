# -*- coding: utf-8 -*-
import math
Cv=int(input('Digite a quantidade de vitórias:'))
Ce=int(input('Digite a quantidade de empates:'))
Cs=int(input('Digite o saldo de gols:'))
Fv=int(input('Digite a quantidade de vitórias:'))
Fe=int(input('Digite a quantidade de empates:'))
Fs=int(input('Digite o saldo de gols:'))

Cv=Cv*3
Fv=Fv*3

if (Cv+Ce)>(Fv+Fe):
    print('C')
elif (Cv+Ce)<(Fv+Fe):
    print('F')
else:
    if Cs>Fs:
        print('C')
    elif Cs<Fs:
        print('F')
    else:
        print('=')